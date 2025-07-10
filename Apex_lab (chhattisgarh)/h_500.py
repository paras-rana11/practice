import os
import time
import socket
import logging
import smtplib
import threading
from email.message import EmailMessage
from datetime import datetime, timedelta

# Configuration variables
CONNECTION_TYPE = 'TCP/IP'
HOST_ADDRESS = '192.168.1.163'  
HOST_PORT = 5600
REPORT_FILE_PREFIX = 'h_500'

REPORT_FILE_PATH = 'C:\\ASTM\\root\\report_file\\'
os.makedirs(REPORT_FILE_PATH, exist_ok=True)

# log file path
LOG_FILE = 'C:\\ASTM\\root\\log_file\\logging_for_h_500_info.log'
ERROR_LOG_FILE = 'C:\\ASTM\\root\\log_file\\logging_for_h_500_error.log'
LOG_FILE_LIST = [LOG_FILE, ERROR_LOG_FILE]

# Email configuration
SUBJECT = 'Email From Apex Hospital'
TO_EMAIL = 'lishealthray@gmail.com'
FROM_EMAIL = 'lishealthray@gmail.com'
PASSWORD = 'rxbr zlzy tpin pgur'

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
    try:
        logger.setLevel(logging.DEBUG)  
        logger.handlers.clear()  

        # Info Handler
        info_handler = logging.FileHandler(log_file)
        info_handler.setLevel(logging.INFO)
        info_format = logging.Formatter('%(asctime)s - INFO - %(message)s')
        info_handler.setFormatter(info_format)

        # Error Handler
        error_handler = logging.FileHandler(error_log_file)
        error_handler.setLevel(logging.ERROR)
        error_format = logging.Formatter('%(asctime)s - ERROR - %(message)s')
        error_handler.setFormatter(error_format)

        logger.addHandler(info_handler)
        logger.addHandler(error_handler)

        return logger
    except Exception as e:
        send_mail_or_logging('Exception in initialize logger', e)
        return logger

logger = setup_loggers(LOG_FILE, ERROR_LOG_FILE)
logger.info('Log file initialized.')
logger.error('This is an error log example.')

def send_mail_or_logging(error_message, error):
    logger.error(f'{error_message} : {error}')

    body = f"""
    Dear Team,

    This is an automated alert from the Laboratory Information System.

        --> {error_message} :: Below are the details of the incident:

        - Filename: horiba_h_500.py
        - Connetion Type: {CONNECTION_TYPE}
        - Machine Name: {REPORT_FILE_PREFIX}
        - IP Address: {HOST_ADDRESS}
        - Port: {HOST_PORT}
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
        send_mail_or_logging('Error in remove old log', e)

def process_data(data):
    # Decode bytes using UTF-8, replacing invalid characters
    try:
        return data.decode('utf-8', errors='replace')

    except Exception as e:
        send_mail_or_logging('Error in process data', e)
        return None

def get_filename():
    try:
        dt = datetime.now()
        return REPORT_FILE_PATH + f"{REPORT_FILE_PREFIX}" + '_' + dt.strftime("%Y-%m-%d-%H-%M-%S-%f")
    except Exception as e:
        send_mail_or_logging('Error in create new file', e)
        return None


def my_read(port):
    try:
        return port.recv(1)
    except Exception as e:
        send_mail_or_logging('Error in read data from port', e)
        return b''

def my_write(port, byte):
    try:
        return port.send(byte)
    except Exception as e:
        send_mail_or_logging('Error in write data to port', e)
        return None

def get_actual_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to a dummy address, doesn't have to be reachable
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

byte_array = []
x = None

def communicate_with_machine():
    global conn
    x = None
    cur_file = None
    try:
        if HOST_ADDRESS == get_actual_ip():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server_socket.bind((HOST_ADDRESS, HOST_PORT))
                server_socket.listen()
                print(f"Server listening on {HOST_ADDRESS}:{HOST_PORT}")
                conn, addr = server_socket.accept()
                print(f"Connected to {addr}")
                while True:
                
                    byte = my_read(conn)
                    if byte == b'':
                        print('<EOF> reached. Connection broken: details below')
                        break

                    if byte == b'\x05':  # Start of Transmission
                        byte_array = [byte.decode('latin1')]
                        my_write(conn, b'\x06')  # Acknowledge
                        cur_file = get_filename()
                        try:
                            x = open(cur_file, 'w', encoding='latin1')
                            x.write(''.join(byte_array))
                        except IOError as e:
                            send_mail_or_logging('Error in open file', e)

                    elif byte == b'\x0a':  # Line Feed
                        my_write(conn, b'\x06')  # Acknowledge
                        try:
                            x = open(cur_file, 'w', encoding='latin1')
                            x.write(''.join(byte_array))
                        except IOError as e:
                            send_mail_or_logging('Error in writing file', e)

                    elif byte == b'\x04':  # End of Transmission
                        try:
                            if x:
                                x.write(''.join(byte_array))
                                x.close()
                                x = None
                                byte_array = []
                                logger.info(f'File closed :- {cur_file}')
                        except Exception as e:
                            error_message = 'Error in closing file'
                            send_mail_or_logging(error_message, e)

                    else:
                        byte_array.append(byte.decode('latin1'))
        else:
            # start_tray()
            pass
    except Exception as e:
        error_message = 'Error in data reading'
        send_mail_or_logging(error_message, e)

    finally:
        logger.info("Closing connection...")
        conn.close()

    threading.Timer(5, communicate_with_machine).start()

# Start the processes
if __name__ == '__main__':
    try:
        threading.Thread(target=remove_old_logs_from_log_file, args=(LOG_FILE_LIST,), daemon=True).start()
        communicate_with_machine()
    except Exception as e:
        error_message = 'Error in main function'
        send_mail_or_logging(error_message, e)