# Here is complate code for register api which is used in bidirectional process
# you only need to change or add machine configuration and condition 
# Rest of all code remain same


from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
from pydantic import BaseModel
from datetime import datetime, timedelta
import requests
import threading
import uvicorn
import os
import pymysql
import time
import json
import logging
import time
import smtplib
from email.message import EmailMessage
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Initialize the FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],  # Allowed HTTP methods
    allow_headers=["*"],  # Allow custom headers like `x-auth-token`, `x-healthray-access-token`
    allow_credentials=False,  # Disallow credentials (cookies, etc.)
)

HOST_ADDRESS = ''
HOST_PORT = 1234

# Mysql Setup
MY_HOST = ''
MY_USER = ''
MY_pass = ''
MY_DB = ''

# log file path
LOG_FILE = 'C:\\ASTM\\root\\log_file\\logging_for_register_patient.log'
ERROR_LOG_FILE = 'C:\\ASTM\\root\\log_file\\logging_for_register_patient_error.log'
LOG_FILE_LIST = [LOG_FILE, ERROR_LOG_FILE]

PAYLOAD_FILE = 'C:\\ASTM\\root\\case_file\\case_payload.json'
CASE_FILE = 'C:\\ASTM\\root\\case_file\\'
os.makedirs(CASE_FILE, exist_ok=True)

# Machine configuration
MACHINE_1_ID = ''
MACHINE_1_COM_PORT = ''
MACHINE_1_HOST_ADDRESS = ''
MACHINE_1_HOST_PORT = 1234
SAMPLE_TYPE_MAPPING_FOR_MACHINE_1 = {
    "serum": "S1",
    "plasma":  "S1",
    "urine": "S2",
    "sodium flouride": "S3",
    "suprnt": "S4",
    "others": "S5",
    "edta whole blood": "S1",
    "edta": "S1",
    "whole blood": "S1"
}

MACHINE_2_ID = ''
MACHINE_2_COM_PORT = ''
MACHINE_2_HOST_ADDRESS = ''
MACHINE_2_HOST_PORT = 1234
SAMPLE_TYPE_MAPPING_FOR_MACHINE_2 = {
    "serum": "S1",
    "plasma":  "S1",
    "urine": "S2",
    "sodium flouride": "S3",
    "suprnt": "S4",
    "others": "S5",
    "edta whole blood": "S1",
    "edta": "S1",
    "whole blood": "S1"
}

# Email configuration
SUBJECT = ''
TO_EMAIL = ''
FROM_EMAIL = ''
PASSWORD = '' 

# Google configuration
GOOGLE_SHEET_NAME = ''
GOOGLE_WORKSHEET_NAME_FOR_LOGGING = ''

CREADENTIAL = {
}

SCOPE = []

creds = ServiceAccountCredentials.from_json_keyfile_dict(CREADENTIAL, SCOPE)  # Load credentials
client = gspread.authorize(creds)  # Authorize client
sheet_log = client.open(GOOGLE_SHEET_NAME).worksheet(GOOGLE_WORKSHEET_NAME_FOR_LOGGING)
sheet_log.update(values=[['Date', 'File_Name', 'Message','Error']], range_name='A1:D1')

# Pydantic model for request body validation
class Case(BaseModel):
    case_id: str
    test_id: list
    machine_id: str
    sample_type: str

class CreateCaseRequest(BaseModel):
    cases: List[Case]

# Method for send email
def send_email(subject, body, to_email, from_email, password):
    try:
        # Create the email message
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email
        msg.set_content(body)

        # Connect to Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()  # Secure the connection
            smtp.login(from_email, password)
            smtp.send_message(msg)

        logger.info('Email sent successfully!')
        return True
    except Exception as e:
        logger.error(f'Failed to send email: {e}')
        return False

# Method for setup logging
def setup_loggers(log_file, error_log_file):
    '''Set up separate loggers for info and error.'''
    logger = logging.getLogger('app_logger')
    logger.setLevel(logging.DEBUG)  # capture everything, filter in handlers
    logger.handlers.clear()  # avoid duplicate logs on reload

    # Info Handler
    info_handler = logging.FileHandler(log_file)
    info_handler.setLevel(logging.INFO)
    info_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    info_handler.setFormatter(info_format)

    # Error Handler
    error_handler = logging.FileHandler(error_log_file)
    error_handler.setLevel(logging.ERROR)
    error_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    error_handler.setFormatter(error_format)

    logger.addHandler(info_handler)
    logger.addHandler(error_handler)

    return logger

logger = setup_loggers(LOG_FILE, ERROR_LOG_FILE)
logger.info('Log file initialized.')
logger.error('This is an error log example.')

# Methid for sending email and logging
def send_mail_or_logging(error_message, error):
    logger.error(f'{error_message} : {error}')

    body = f"""
    Dear Team,

    This is an automated alert from the Laboratory Information System.

        --> {error_message} :: Below are the details of the incident:

        - Filename: register_patient.py
        - Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

        - Error Details: {error}

    Best regards,  
    Laboratory Information System  
    [Healthray LAB]
    """

    is_send_mail = send_email(SUBJECT, body, TO_EMAIL, FROM_EMAIL, PASSWORD)
    if not is_send_mail:
        logger.error(f"Exception during sending mail")

def remove_old_logs_from_log_file(log_file_list):
    try:
        logger.info("Thread Start For Remove old Logs")
        while True:
            for file in log_file_list:
                with open(file, 'r') as f:
                    data = f.read()

                lines = data.split('\n')

                cutoff_date = datetime.now() - timedelta(days=10)
                final_line_list = []
                for line in lines:
                    line_date = line.split()
                    if len(line_date) > 1:
                        if line_date[0] > (str(cutoff_date)).split()[0]:
                            final_line_list.append(line)

                with open(file,'w') as f:
                    f.write('\n'.join(final_line_list))
            
            time.sleep(86400)
    except Exception as e:
        error_message = 'Error in remove old log'
        send_mail_or_logging(error_message, e)

# Function to process a single case
def process_case(case: Dict[str, Any], case_id: str, responses: List[Dict[str, Any]]):
    try:
        test_id = case.get("test_id")
        machine_id = case.get("machine_id")

        if not all([case_id, test_id, machine_id]):
            responses.append({
                "status": 400,
                "statusState": "error",
                "message": f"Missing required data for case_id {case_id}. Expected: test_id, machine_id."
            })
            error_message = 'Error in remove old log'
            send_mail_or_logging(error_message, e)
            return

        # Handle sample type and reformat test_id
        if machine_id == MACHINE_1_ID:
            sample_type = case.get("sample_type", "").lower()
            for key, value in SAMPLE_TYPE_MAPPING_FOR_MACHINE_1.items():
                if key in sample_type:
                    case["sample_type"] = value
                    break
            formatted_test_id = "^^^" + "^\\^^^".join(test_id) + "^"
            case["test_id"] = formatted_test_id

            # Send the case to another service via HTTP POST
            try:
                response = requests.post(f"http://{MACHINE_1_HOST_ADDRESS}:{MACHINE_1_HOST_PORT}/create_case/{MACHINE_1_COM_PORT}", json=case)
                case_entry = {
                    "case_id": case_id,
                    "sample_type": sample_type,
                    "response": response.status_code,
                    "api": f"http://{MACHINE_1_HOST_ADDRESS}:{MACHINE_1_HOST_PORT}/create_case/{MACHINE_1_COM_PORT}",
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                save_case_to_json(case_entry, machine_id, 'log_api.json')
                if response.status_code == 200:
                    responses.append({
                        "status": 200,
                        "statusState": "success",
                        "message": f"Case Creation Process Started for machine {machine_id}",
                        "case_id": case_id,
                    })
                else:
                    case_entry = {
                        "case_id": case_id,
                        "sample_type": sample_type,
                        "response": response.status_code,
                        "api": f"http://{MACHINE_1_HOST_ADDRESS}:{MACHINE_1_HOST_PORT}/create_case/{MACHINE_1_COM_PORT}",
                        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    save_case_to_json(case_entry, machine_id, 'log_api_fail.json')
                    responses.append({
                        "status": 400,
                        "statusState": "error",
                        "case_id": case_id,
                        "message": f"Failed to create case {case_id} for machine_id {machine_id}. Status code: {response.status_code}",
                    })

                    error_message = f"Failed to create case {case_id} for machine_id {machine_id}. Status code: {response.status_code}"
                    error = 'Failed to create case'
                    send_mail_or_logging(error, error_message)

            except requests.exceptions.RequestException as e:
                responses.append({
                    "status": 400,
                    "statusState": "error",
                    "case_id": case_id,
                    "message": f"Request to create case {case_id} failed: {str(e)}",
                })

                error_message = f"Request to create case {case_id} failed: {str(e)}"
                send_mail_or_logging(error_message, e)

        elif machine_id == MACHINE_2_ID:
            sample_type = case.get("sample_type", "").lower()
            for key, value in SAMPLE_TYPE_MAPPING_FOR_MACHINE_2.items():
                if key in sample_type:
                    case["sample_type"] = value
                    break
            formatted_test_id = "^^^" + "^\\^^^".join(test_id) + "^"
            case["test_id"] = formatted_test_id
        
            # Send the case to another service via HTTP POST
            try:
                response = requests.post(f"http://{MACHINE_2_HOST_ADDRESS}:{MACHINE_2_HOST_PORT}/create_case/{MACHINE_2_COM_PORT}", json=case)
                case_entry = {
                    "case_id": case_id,
                    "sample_type": sample_type,
                    "response": response.status_code,
                    "api": f"http://{MACHINE_2_HOST_ADDRESS}:{MACHINE_2_HOST_PORT}/create_case/{MACHINE_2_COM_PORT}",
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                save_case_to_json(case_entry, machine_id, 'log_api.json')
                if response.status_code == 200:
                    responses.append({
                        "status": 200,
                        "statusState": "success",
                        "message": f"Case Creation Process Started for machine {machine_id}",
                        "case_id": case_id,
                    })
                else:
                    case_entry = {
                        "case_id": case_id,
                        "sample_type": sample_type,
                        "response": response.status_code,
                        "api": f"http://{MACHINE_2_HOST_ADDRESS}:{MACHINE_2_HOST_PORT}/create_case/{MACHINE_2_COM_PORT}",
                        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    save_case_to_json(case_entry, machine_id, 'log_api_fail.json')
                    responses.append({
                        "status": 400,
                        "statusState": "error",
                        "case_id": case_id,
                        "message": f"Failed to create case {case_id} for machine_id {machine_id}. Status code: {response.status_code}",
                    })

                    error_message = f"Failed to create case {case_id} for machine_id {machine_id}. Status code: {response.status_code}"
                    error = 'Failed to create case'
                    send_mail_or_logging(error, error_message)

            except requests.exceptions.RequestException as e:
                responses.append({
                    "status": 400,
                    "statusState": "error",
                    "case_id": case_id,
                    "message": f"Request to create case {case_id} failed: {str(e)}",
                })
                error_message = f"Request to create case {case_id} failed: {str(e)}"
                send_mail_or_logging(error_message, e)

        else:
            responses.append({
                "status": 400,
                "statusState": "error",
                "case_id": case_id,
                "message": f"Invalid machine_id {machine_id} for case_id {case_id}",
            })

            error_message = 'Error in create case'
            error = 'Machine id not found'
            send_mail_or_logging(error_message, error)

    except Exception as e:
        responses.append({
            "status": 400,
            "statusState": "error",
            "case_id": case_id,
            "message": f"Unexpected error while processing case {case_id}: {str(e)}",
        })
        error_message = 'Error in process case'
        send_mail_or_logging(error_message, e)

# Method for save case entry in json file
def save_case_to_json(case_entry, machine_id, file_name):
    """Save case information to a JSON file, preserving data from the last 10 days and adding new entries."""
    file_path = os.path.join(CASE_FILE, file_name)

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

        # Calculate the cutoff date for retaining entries
        cutoff_date = datetime.now() - timedelta(days=10)

        # Clean up old entries
        for machine_group in existing_data:
            for machine in machine_group:
                if machine_id in machine:
                    # Filter entries by checking the timestamp
                    machine[machine_id] = [
                        entry for entry in machine[machine_id]
                        if datetime.strptime(entry["timestamp"], '%Y-%m-%d %H:%M:%S') > cutoff_date
                    ]

        # Check if the machine already exists and add the new entry if needed
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

        # If the machine ID is not found, create a new entry for this machine
        if not machine_found:
            existing_data[0].append({machine_id: [case_entry]})

        # Save the updated data back to the file
        with open(file_path, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)

    except Exception as e:
        error_message = 'Error in save case in json file case'
        send_mail_or_logging(error_message, e)

# Method for load new json file 
def load_json(file_path):
    try:
        # Open the file and load existing data
        if os.path.exists(file_path):
            with open(file_path, 'r') as json_file:
                try:
                    existing_data = json.load(json_file)
                except json.JSONDecodeError:
                    existing_data = [[]]
        else:
            with open(file_path, 'w') as json_file:
                json.dump([[]], json_file, indent=4)
            existing_data = [[]]
        return existing_data
    
    except Exception as e:
        existing_data = [[]]
        error_message = 'Error in loding json file'
        send_mail_or_logging(error_message, e)
        return existing_data

# Method for dump json data in file
def save_json(file_path, data):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        error_message = 'Error in saving data in json file'
        send_mail_or_logging(error_message, e)

# Method for add new payload entry in file
def add_new_payload_entry(case_data, payload_file):
    try:
        payload_data = load_json(payload_file)
        if payload_data != [[]]:
            payload_data_list = payload_data[0][0]["cases"]
            for case_data_item in case_data:
                case_dict = case_data_item.__dict__
                case_dict["timestamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                payload_data_list.append(case_dict)

            save_json(payload_file, payload_data)
            with open(payload_file, 'w') as f:
                json.dump(payload_data, f, indent=4)
        else:
            payload_case_list = []
            for case_data_item in case_data:
                case_dict = case_data_item.__dict__
                case_dict["timestamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                payload_case_list.append(case_dict)
            payload_data[0].append({'cases':payload_case_list})
            save_json(payload_file, payload_data)
    except Exception as e:
        error_message = 'Error in add new payload entry'
        send_mail_or_logging(error_message, e)

# Method for remove old payload entry
def remove_old_payload_entry(payload_file):
    try:
        while True:
            payload_file_data = load_json(payload_file)
            if payload_file_data != [[]]:
                new_case_list = [] 

                cutoff_date = datetime.now() - timedelta(days=7)

                json_data_list = payload_file_data[0][0]["cases"]
                for case in json_data_list:
                    if datetime.strptime(case["timestamp"], '%Y-%m-%d %H:%M:%S') > cutoff_date:
                        new_case_list.append(case)

                payload_file_data[0][0]["cases"] = new_case_list

                with open(payload_file, 'w') as f:
                    json.dump(payload_file_data, f, indent=4)

            time.sleep(86400)
    
    except Exception as e:
        error_message = 'Error in remove old payload entry'
        send_mail_or_logging(error_message, e)

# API endpoint to create cases
@app.post("/create_case")
async def api_create_case(request: CreateCaseRequest):
    payload_data = []
    try:
        data = request.cases  # List of cases
        payload_data.append(data)
        responses = []
        
        
        if not data:
            error_message = 'Error in create case api calling'
            error = 'No data found'
            send_mail_or_logging(error_message, error)
            return JSONResponse(
                content={
                    "status": 400,
                    "statusState": "error",
                    "data": responses,
                    "message": "No data provided",
                }
            )
        
        add_new_payload_entry(data, PAYLOAD_FILE)
        
        pending_cases = {}
        threads = []
        for case in data:
            case_id = case.case_id
            machine_id = case.machine_id
            if not case_id:
                responses.append({
                    "status": 400,
                    "statusState": "error",
                    "message": "Missing case_id in the request",
                })
                continue
            case_entry = {
                "case_id": case_id,
                "api": f"http://{HOST_ADDRESS}:{HOST_PORT}/create_case",
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            save_case_to_json(case_entry, machine_id, 'log_main_api.json')
            thread = threading.Thread(target=process_case, args=(case.model_dump(), case_id, responses))
            pending_cases[case_id] = thread
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        return JSONResponse(
            content={
                "status": 200,
                "statusState": "success",
                "data": responses,
                "message": "Process Started",
            }
        )
    except Exception as e:
        case_entry = {
            "api": f"http://{HOST_ADDRESS}:{HOST_PORT}/create_case",
            "payload_data": payload_data,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        save_case_to_json(case_entry, "LAB Machine", 'log_main_api_fail.json')

        error_message = 'Error in create case api calling'
        send_mail_or_logging(error_message, e)

        return JSONResponse(
            content={
                "status": 400,
                "statusState": "error",
                "data": [],
                "message": f"Internal Threading Error : {e}",
            }
        )

# API endpoint to get patient data
@app.get("/get_patient_data")
async def get_patient_data(pid: str = Query(None)):
    try:
        if pid:
            conn = pymysql.connect(
                host=MY_HOST,
                user=MY_USER,
                password=MY_pass,
                database=MY_DB,
                cursorclass=pymysql.cursors.DictCursor  # Using DictCursor for returning results as dictionaries
            )
            cursor = conn.cursor()
            query = f"SELECT * FROM machineData WHERE patientId = '{pid}'"
            cursor.execute(query)
            result = cursor.fetchall()

            cursor.close()
            conn.close()

            if result:
                response = {
                    "data": result,
                    "message": "LIS results retrieved successfully",
                    "statusState": "success",
                    "status": 200
                }
            
            else:
                response = {
                    "data": [],
                    "message": "Report Not Ready",
                    "statusState": "success",
                    "status": 200
                }
        else:
            # Case when pid is not provided
            response = {
                "data": [],
                "message": "Case ID Not Found",
                "statusState": "fail",
                "status": 422
            }

        return JSONResponse(content=response)

    except Exception as e:
        response = {
            "data": [],
            "message": "Internal Server Error",
            "statusState": "error",
            "status": 500
        }

        error_message = 'Error in get patient data api call'
        send_mail_or_logging(error_message, e)

        return JSONResponse(content=response)

# Run the app with Uvicorn if executed directly
if __name__ == "__main__":
    try:
        threading.Thread(target=remove_old_logs_from_log_file, args=(LOG_FILE_LIST,), daemon=True).start()
        threading.Thread(target=remove_old_payload_entry, args=(PAYLOAD_FILE,), daemon=True).start()
        uvicorn.run(app, host=HOST_ADDRESS, port=HOST_PORT)
    except Exception as e:
        error_message = 'Error in main function'
        send_mail_or_logging(error_message, e)