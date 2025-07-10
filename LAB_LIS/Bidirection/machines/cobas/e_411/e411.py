from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pydantic import BaseModel
from typing import Optional
from threading import RLock, Thread
from datetime import datetime, timedelta
import uvicorn
import time
import json
import os
import logging

from helper import MachineConnectionSerial, GenerateChecksum

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global objects and variables
generate_checksum = GenerateChecksum()
LOCK = RLock()
STOP_THREAD = False

connection_e_411 = MachineConnectionSerial(
    connection_type="serial",
    input_tty="COM3", 
    machine_name="e_411_"
)
# Try to establish connection
port_e_411, path = connection_e_411.get_port()

# Initialize FastAPI app
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle lifespan events."""
    # Startup event
    start_receiving_data(connection_e_411)
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request schema for create_case
class CreateCaseRequest(BaseModel):
    case_id: str
    test_id: str
    sample_type: str
    machine_id: str

# Helper functions
def send_message(connection, message):
    """Send a framed message with checksum to the machine."""
    framed_message = f"{generate_checksum.STX}{message}{generate_checksum.CR}{generate_checksum.ETX}"
    checksum = generate_checksum.get_checksum_value(framed_message)
    final_message = f"{framed_message}{checksum}{generate_checksum.CR}{generate_checksum.LF}"
    connection.write(final_message.encode())


def write_data_to_file(file, byte_array):
    """Write data to a file safely."""
    try:
        file.write(''.join(byte_array))
    except Exception as e:
        print(f"Error writing to file: {e}")
        raise


def create_case_in_machine(connection, case_no, test_id, sample_type):
    """Send commands to the machine to create a case."""
    with LOCK:
        try:
            logging.info("CASE CREATION PROCESS STARTED")
            connection.write(generate_checksum.ENQ.encode())
            byte = connection.read()

            if byte == generate_checksum.ACK.encode():
                # Step 1: Send header message
                header_message = f"1H|\^&|||host^1|||||cobas-e411|TSDWN^BATCH|P|1"
                send_message(connection, header_message)
                if connection.read() != generate_checksum.ACK.encode():
                    return {"status": "error", "message": "Header Message Not Acknowledged"}
                logging.info(f"HEADER MESSAGE :-  {header_message}")

                # Step 2: Send patient message
                patient_message = f"2P|1"
                send_message(connection, patient_message)
                if connection.read() != generate_checksum.ACK.encode():
                    return {"status": "error", "message": "Patient Message Not Acknowledged"}
                logging.info(f"PATIENT MESSAGE :-  {patient_message}")

                # Step 3: Send order message
                order_message = (
                    f"3O|1|{case_no}|^^^^{sample_type}^SC|{test_id}|R||||||A||||1||||||||||O"
                    
                )
                send_message(connection, order_message)
                if connection.read() != generate_checksum.ACK.encode():
                    return {"status": "error", "message": "Order Message Not Acknowledged"}
                logging.info(f"ORDER MESSAGE :-  {order_message}")

                # Step 4: Send termination message
                termination_message = f"4L|1|N"
                send_message(connection, termination_message)
                if connection.read() == generate_checksum.ACK.encode():
                    connection.write(generate_checksum.EOT.encode())
                    logging.info(f"TERMINATION MESSAGE :-  {termination_message}")
                    return {"status": "success", "message": "Case created successfully"}
                else:
                    return {"status": "error", "message": "Termination Message Not Acknowledged"}
            else:
                return {"status": "error", "message": "ENQ Message Not Acknowledged"}
        except Exception as e:
            return {"status": "error", "message": str(e)}


def save_case_to_json(case_entry, machine_id, file_name):
    """Save case information to a JSON file, preserving data from the last 10 days and adding new entries."""
    file_path = os.path.join('C:\\ASTM\\root\\case_file\\', file_name)
    os.makedirs('C:\\ASTM\\root\\case_file\\', exist_ok=True)

    try:
        # Open the file and load existing data
        if os.path.exists(file_path):
            with open(file_path, 'r') as json_file:
                try:
                    existing_data = json.load(json_file)
                except json.JSONDecodeError:
                    existing_data = [[]]
        else:
            existing_data = [[]]

        cutoff_date = datetime.now() - timedelta(days=10)

        for machine_group in existing_data:
            for machine in machine_group:
                if machine_id in machine:
                    machine[machine_id] = [
                        entry for entry in machine[machine_id]
                        if datetime.strptime(entry["timestamp"], '%Y-%m-%d %H:%M:%S') > cutoff_date
                    ]

        machine_found = False
        for machine_group in existing_data:
            for machine in machine_group:
                if machine_id in machine:
                    # Avoid duplicates
                    if not any(entry["case_id"] == case_entry["case_id"] for entry in machine[machine_id]):
                        machine[machine_id].append(case_entry)
                    machine_found = True
                    break
            if machine_found:
                break

        if not machine_found:
            existing_data[0].append({machine_id: [case_entry]})

        with open(file_path, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)

    except Exception as e:
        print(f"Error saving JSON to file: {e}")


def retry_api_call(connection, case_id, test_id, sample_type, machine_id):
    """Retry API call to ensure the case is created."""
    counter = 0
    while True:
        try:
            response = create_case_in_machine(connection, case_id, test_id, sample_type)
            if response["status"] == "success":
                case_entry = {"case_id": case_id, "test_id": test_id, "sample_type": sample_type, "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                save_case_to_json(case_entry, machine_id, 'log_complate_case.json')
                logging.info(f"COUNTER :- {counter}")
                return response
        except Exception as e:
            print(f"Error in API call: {e}")
            case_entry = {"case_id": case_id, "test_id": test_id, "sample_type": sample_type, "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "status":"Error"}
            save_case_to_json(case_entry, machine_id, 'log_error_case.json')
        counter+=1
        time.sleep(5)


def continuous_receiving_data(connection):
    """Continuously receive data from the machine."""
    global STOP_THREAD
    byte_array = []
    file = None  # Initialize file variable here

    logging.info("Started unidirectional reading...")
    while not STOP_THREAD:
        with LOCK:
            if connection:
                try:
                    byte = connection.read()
                    if not byte:
                        continue

                    byte_array.append(chr(ord(byte)))
                    # print(f"Received byte: {byte} = {ord(byte)}")

                    if byte == b'\x05':  # Start of new data
                        byte_array = [chr(ord(byte))]
                        connection.write(b'\x06')  # Send ACK
                        cur_file = connection.get_filename()
                        try:
                            if file:  # Close any open file before opening a new one
                                file.close()
                            file = open(cur_file, 'w')  # Open a new file
                            write_data_to_file(file, byte_array)
                        except IOError as ioe:
                            print(f"Error opening file {cur_file}: {ioe}")
                    elif byte == b'\x0a':  # Data block finished
                        connection.write(b'\x06')  # Send ACK
                        write_data_to_file(file, byte_array)
                        byte_array = []
                    elif byte == b'\x04':  # End of data transmission
                        if file:  # Check if file is open before writing
                            write_data_to_file(file, byte_array)
                            print('Data written to file, closing...')
                            file.close()
                        byte_array = []

                except Exception as e:
                    print(f"Error in unidirectional reading: {e}")
    print("Stopped unidirectional reading.")


def start_receiving_data(connection):
    """Start data receiving thread."""
    try:
        receive_thread = Thread(target=continuous_receiving_data, args=(connection,))
        receive_thread.daemon = True
        receive_thread.start()
    except Exception as e:
        print(f"Error starting receiving thread: {e}")


# API routes
@app.post("/create_case/COM3")
async def api_create_case(request: CreateCaseRequest, background_tasks: BackgroundTasks):
    """API endpoint to create a case."""
    try:
        background_tasks.add_task(
            retry_api_call,
            connection_e_411,
            request.case_id,
            request.test_id,
            request.sample_type,
            request.machine_id
        )
        return {"status": 200, "statusState": "success", "message": "Case Creation Started"}
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={
                "status": 400,
                "statusState": "error",
                "message": f"Case Creation Error: {e}"
            }
        )

# Main
if __name__ == "__main__":
    # start_receiving_data(connection_e_411)
    uvicorn.run(app, host="0.0.0.0", port=5002)
