import json
import os
import re
import time
import pymysql
import requests
import jwt
from datetime import datetime, timedelta, timezone
import ast
import logging
import smtplib
import threading
import shutil
from email.message import EmailMessage
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# Mysql Configuration
MY_HOST = '127.0.0.1'
MY_USER = 'root'
MY_PASS = 'Root@1234'
MY_DB = 'lis'

# Report file path
REPORT_FILE_PATH = 'C:\\ASTM\\root\\report_file\\'
BACKUP_FILE_PATH = 'C:\\ASTM\\root\\backup_file\\'

# log file path
LOG_FILE = 'C:\\ASTM\\root\\log_file\\logging_for_database_info.log'
ERROR_LOG_FILE = 'C:\\ASTM\\root\\log_file\\logging_for_database_error.log'
LOG_FILE_LIST = [LOG_FILE, ERROR_LOG_FILE]

# Email configuration
SUBJECT = 'Email From Apex Hospital'
TO_EMAIL = 'lishealthray@gmail.com'
FROM_EMAIL = 'lishealthray@gmail.com'
PASSWORD = 'rxbr zlzy tpin pgur' 

# Cloud configuration
LAB_BRANCH_ID = 465
LAB_URL = 'https://labapi.healthray.com/api/v1/lis_case_result'
JWT_SECRET_KEY = 'pr0@sc.j%fK*yJ$=f^Bi5gF8isQLS&$d'

# Method for setup logging
def setup_loggers(log_file, error_log_file):
    '''Set up separate loggers for info and error.'''
    logger = logging.getLogger('app_logger')
    try:
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
    except Exception as e:
        print(f"Error in initialize logger : {e}")
        return logger


logger = setup_loggers(LOG_FILE, ERROR_LOG_FILE)
logger.info('Log file initialized.')
logger.error('This is an error log example.')

# Method for sending email and logging
def send_mail_or_logging(error_message, error):
    logger.error(f'{error_message} : {error}')

    body = f"""
    Dear Team,

    This is an automated alert from the Laboratory Information System.

        --> {error_message} :: Below are the details of the incident:

        - Filename: database.py
        - Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

        - Error Details: {error}

    Best regards,  
    Laboratory Information System  
    [Healthray LAB]
    """

    is_send_mail = send_email(SUBJECT, body, TO_EMAIL, FROM_EMAIL, PASSWORD)
    if not is_send_mail:
        logger.error(f"Exception during sending mail")

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

# Method for reading txt file
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        error_message = 'Error in reading file'
        send_mail_or_logging(error_message, e)
        return None

# Method for connection establish to mysql
def get_connection():
    try:
        con = pymysql.connect(
            host=MY_HOST,
            user=MY_USER,
            password=MY_PASS,
            database=MY_DB
        )
        return con
    except pymysql.MySQLError as e:
        error_message = 'Error in establish connection'
        send_mail_or_logging(error_message, e)
        return None

# Method for run query
def run_query(con, prepared_sql, data_tpl):
    try:
        with con.cursor() as cur:
            cur.execute(prepared_sql, data_tpl)
            con.commit()
            return cur
    except pymysql.MySQLError as e:
        error_message = 'Error in query'
        send_mail_or_logging(error_message, e)
        return None

# Method for close cursor
def close_cursor(cur):
    try:
        if cur:
            cur.close()
    except pymysql.MySQLError as e:
        error_message = 'Error in closing cursor'
        send_mail_or_logging(error_message, e)

# Method for close connection
def close_connection(con):
    try:
        if con:
            con.close()
    except pymysql.MySQLError as e:
        error_message = 'Error in closing connection'
        send_mail_or_logging(error_message, e)

# Method for save data in mysql 
def send_to_mysql(data):
    try:
        con = get_connection()
        if not con:
            return False
        prepared_sql = 'INSERT INTO machineData (machineName, patientId, test) VALUES (%s, %s, %s)'
        try:
            json_report_data = json.dumps(data[2]) if data[2] else json.dumps({})
            cur = run_query(con, prepared_sql, (data[0], data[1], json_report_data))
            if cur:
                close_cursor(cur)
        except Exception as e:
            error_message = 'Error in save in mysql'
            send_mail_or_logging(error_message, e)
            return False
        finally:
            close_connection(con)
        return True
    except Exception as e:
        error_message = 'Error in save in mysql'
        send_mail_or_logging(error_message, e)
        return False

def remove_control_characters(text):
    try:
        # Step 2: Remove STX ENQ, ETX+1char, EOT, ETB+2char
        text = re.sub(r"\x02.", "", text) 
        text = re.sub(r"\x05", "", text)   
        text = re.sub(r"\x03.", "", text)  
        text = re.sub(r"\x04", "", text)       
        text = re.sub(r"\x17..", "", text)  

        # Strip spaces from each line
        text = "\n".join(line.strip() for line in text.splitlines())
        return text
    except Exception as e:
        error_message = 'Error in remove control characters'
        send_mail_or_logging(error_message, e)
        return None

def merge_broken_lines(text):
    try:
        lines = text.splitlines()
        merged_lines = []
        fixed_lines = []

        for line in lines:
            line = line.strip()
            if merged_lines and not re.match(r'^[A-Z]\|\d+\|', line) and not re.match(r'^[HLPRCO]\|', line):
                merged_lines[-1] += line  # continuation of previous line
            else:
                merged_lines.append(line)

        for line in merged_lines:
            if re.match(r'^C\|1\|I\|.*R\|\d+\|', line):
                # Find the part where "R|n|" starts
                match = re.search(r'(R\|\d+\|)', line)
                if match:
                    split_index = match.start()
                    corrupted_c = line[:split_index]
                    fixed_r = line[split_index:]
                    fixed_lines.append(corrupted_c)
                    fixed_lines.append(fixed_r)
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)    

        return fixed_lines

    except Exception as e:
        error_message = 'Error in merge broken line function'
        send_mail_or_logging(error_message, e)
        return []

def extract_report_data_mispa_nano(data):
    patients = [] 
    try:
        cleaned_data = remove_control_characters(data)

        # Step 2: Merge broken lines
        merged_lines = merge_broken_lines(cleaned_data)

        if merged_lines:
            machine_name = 'MISPA_NANO_PLUS'
            
            patient_name = None
            report_data = {}

            for line in merged_lines:
                if line.startswith('O'):
                    if patient_name and report_data:
                        patients.append((machine_name, patient_name, str(report_data)))
                        report_data = {}
                        patient_name = None
                    patient_name = line.split('|')[3]
                    if '-' in patient_name:
                        patient_name = patient_name.split('-')[0]

                elif line.startswith('R'):
                    report_name = line.split('|')[2]
                    report_value = line.split('|')[3].replace('^', '').strip()
                    report_data[report_name] = report_value

            # Append the last patient's data after the loop
            if patient_name and report_data:
                patients.append((machine_name, patient_name, str(report_data)))

            return patients
    except Exception as e:
        error_message = 'Error in extract data from mispa nano plus'
        send_mail_or_logging(error_message, e)
        return patients

def remove_starting_chars(data):
    try:
      return [re.sub(r'^\x05|\x03|\x02', '', item) for item in data]
    except Exception as e:
        send_mail_or_logging('Error in healper function', e)
        return []
    
# Method for Horiba H 500 Machine
def extract_report_data_horiba_h_500(data):
    patients = []
    try:
        lines = data.split('\n')
        lines = remove_starting_chars(lines)
        patientId = None
        machine_name = 'H_500'
        result_dict = {}

        for line in lines:
            
            if line.startswith('2P'):
                if len(line.split('|'))>3:
                    patientId = line.split('|')[3]
            elif re.match(r'^[0-9]R\|',line):
                if len(line.split('|'))>3:
                    test_name = line.split('|')[2].split('^')[3]
                    test_result = line.split('|')[3]
                    result_dict[test_name] = test_result

        if patientId and result_dict:
            patients.append((machine_name, patientId, str(result_dict)))
        return patients
    except Exception as e:
        send_mail_or_logging('Error in extract data from horiba h 500', e)
        return patients

def extract_report_data_from_aia_360(data):
    patients = []
    try:
        machine_name = 'AIA_360'
        case_no = None
        report_data = {}

        lines = data.split('\n')

        for line in lines:
            line_data = line.split(',')
            if len(line_data) > 6:
                if case_no and report_data:
                    patients.append((machine_name, case_no, str(report_data)))
                    case_no = None
                    report_data = {}
                case_no = line_data[1].strip()
                test_name = line_data[3].replace('#','').strip()
                test_value = line_data[5].strip()

                report_data[test_name] = test_value

        if case_no and report_data:
            patients.append((machine_name, case_no, str(report_data)))
        return patients
    except Exception as e:
        send_mail_or_logging('Error in extract data from aia 360', e)
        return patients
        
# Method for extract data from txt file and remove used txt file  
def extract_list_data_from_txt_file(folder_path, backup_path):
    file_path = None
    results = []
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            text_data = read_file(file_path)
            if not text_data:
                continue
            extractors = {
                'mispa_nano_plus_': extract_report_data_mispa_nano,
                'h_500_': extract_report_data_horiba_h_500,
                'aia_360_': extract_report_data_from_aia_360          
            }
            extractor = next((ext for prefix, ext in extractors.items() if filename.startswith(prefix)), None)
            if extractor:
                results.append(extractor(text_data))
                try:
                    shutil.copy2(file_path, backup_path)
                    os.remove(file_path)
                    file_path = None
                except Exception as e:
                    if 'The process cannot access the file because it is being used by another process' not in str(e):
                        error_message = 'Error in removing file'
                        send_mail_or_logging(error_message, e)
            else:
                try:
                    shutil.copy2(file_path, backup_path)
                    os.remove(file_path)
                    file_path = None
                except Exception as e:
                    if 'The process cannot access the file because it is being used by another process' not in str(e):
                        error_message = 'Error in removing file'
                        send_mail_or_logging(error_message, e)
        return results
    except Exception as e:
        error_message = 'Error in extract data from txt file'
        send_mail_or_logging(error_message, e)
        return results
    finally:
        try:
            if file_path:
                shutil.copy2(file_path, backup_path)
                os.remove(file_path)
                file_path = None
        except Exception as e:
            if 'The process cannot access the file because it is being used by another process' not in str(e):
                error_message = 'Error in removing file'
                send_mail_or_logging(error_message, e)
            
# Method for send patient data to healthray lab
def send_to_healthray(results):
    try:
        url = LAB_URL

        expiry_time = datetime.now(timezone.utc) + timedelta(seconds=45)
        payload = {
            'data': {
                'platform': 'Python',
                'branch_id': LAB_BRANCH_ID 
            },
            'exp': expiry_time
        }
        jwt_token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
        header = {
            'authorization': f'{jwt_token}',
            'Content-Type': 'application/json'
        }

        output_dict = {
            'patient_case_results': [
                {
                    'lab_branch_id': LAB_BRANCH_ID,
                    'lis_machine_id': sub_item[0],
                    'patient_case_no': sub_item[1],
                    'result': sub_item[2]
                }
                for item in results for sub_item in item
            ]
        }
        response = requests.post(url, headers=header, json=output_dict)
        if response is None:
            error_message = 'Error in api call'
            send_mail_or_logging(error_message, "None")
            return None

        if response.status_code == 200:
            return response.json() 
        else:
            error_message = 'Error in api calling'
            send_mail_or_logging(error_message, response.status_code)
            return None

    except Exception as e:
        error_message = 'Error in send data to healthray'
        send_mail_or_logging(error_message, e)
        return None

# Method for save data in mysql db
def send_data_to_mysql(results):
    case_no_list = []
    google_data_list = []
    try:
        flattened_list = [sub_list for item in results for sub_list in item]
        if isinstance(flattened_list, list):
            for result in flattened_list:
                result = list(result)
                google_data_list.append(result)
                data_dict = result[2]
                case_no = result[1]
                data_dict = ast.literal_eval(data_dict)
                result[2] = data_dict
                result = tuple(result)
                send_to_mysql(result)       
                case_no_list.append(case_no) 
        else:
            pass
        return case_no_list, google_data_list
    except Exception as e:
        error_message = 'Error in send data to mysql'
        send_mail_or_logging(error_message, e)
        return case_no_list, google_data_list

# Thread for remove old log 
threading.Thread(target=remove_old_logs_from_log_file, args=(LOG_FILE_LIST,), daemon=True).start()

# main loop
while True:
    try:
        all_results = extract_list_data_from_txt_file(REPORT_FILE_PATH, BACKUP_FILE_PATH)
        if all_results:
            case_no, google_data = send_data_to_mysql(all_results)
            logger.info(f'Data Save in MySQL For {case_no}')
            save_to_healthray_lab = send_to_healthray(all_results) 
            logger.info(f'Data Save in Cloud For {save_to_healthray_lab}')

        time.sleep(8)
    except Exception as e:
        error_message = 'Error in main loop'
        send_mail_or_logging(error_message, e)
