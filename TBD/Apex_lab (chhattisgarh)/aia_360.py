import time
import serial # type: ignore
import logging
import smtplib
import threading
from email.message import EmailMessage
from datetime import datetime, timedelta

CONNECTION_TYPE = 'Serial'
COM_PORT = 'COM4'
BAUDRATE = 19200
TIMEOUT = 1
REPORT_FILE_PREFIX = 'aia_360'
CONNECTION_OBJECT = None
x = None

REPORT_FILE_PATH = 'C:\\ASTM\\root\\report_file\\'

# log file path
LOG_FILE = 'C:\\ASTM\\root\\log_file\\logging_for_aia_360_info.log'
ERROR_LOG_FILE = 'C:\\ASTM\\root\\log_file\\logging_for_aia_360_error.log'
LOG_FILE_LIST = [LOG_FILE, ERROR_LOG_FILE]

# Email configuration
SUBJECT = 'Email From Apex Hospital(Chhatisgarh)'
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

        - Filename: aia_360.py
        - Connetion Type: {CONNECTION_TYPE}
        - Serial Port: {COM_PORT}
        - Machine Name: {REPORT_FILE_PREFIX}
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

class Connection:

    def __init__(self, com_port: str, baudrate: int, timeout: int, report_file_path: str, report_file_prefix: str):
        self.connection = None
        self.com_port = com_port
        self.baudrate = baudrate
        self.timeout = timeout
        self.report_file_path = report_file_path
        self.report_file_prefix = report_file_prefix

    def get_connection(self):
        try:
            self.connection = serial.Serial(port=self.com_port, baudrate=self.baudrate, timeout=self.timeout)
            logger.info(self.connection)
            if self.connection:
                return self.connection
            else:
                return None
        except Exception as e:
            error_message = 'Error in Connection'
            send_mail_or_logging(error_message, e)

    def close_connection(self):
        try:
            if self.connection:
                self.connection.close()
                self.connection = None
        except Exception as e:
            error_message = 'Error in Connection'
            send_mail_or_logging(error_message, e)

    def read_byte(self):
        try:
            if self.connection:
                byte = self.connection.read(1)
                return byte
            else:
                logger.info("Connection Not Made")
                return None
        except Exception as e:
            error_message = 'Error in Connection'
            send_mail_or_logging(error_message, e)

    def write_byte(self, byte):
        try:
            if self.connection:
                self.connection.write(byte)
            else:
                logger.info("Connection Not Made")
        except Exception as e:
            error_message = 'Error in Connection'
            send_mail_or_logging(error_message, e)

    def get_filename(self):
        try:
            return self.report_file_path + self.report_file_prefix + '_' + datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
        except Exception as e:
            error_message = 'Error in get_filename'
            send_mail_or_logging(error_message, e)

def communicate_with_machine():
    global CONNECTION_OBJECT
    cur_file = None
    byte_array = []
    try:
        while True:
            try:
                if CONNECTION_OBJECT.connection:
                    byte = CONNECTION_OBJECT.read_byte()
                    if not byte:
                        pass
                    else:
                        byte_array.append(chr(ord(byte)))

                    if byte_array and not byte:
                        cur_file = CONNECTION_OBJECT.get_filename()
                        try:
                            x = open(cur_file, 'w')
                            x.write(''.join(byte_array))
                            x.close()
                            byte_array = []
                            print(f'File closed :- {cur_file}')
                        except IOError as e:
                            error_message = 'Error in txt file initialize'
                            send_mail_or_logging(error_message, e)
                else:
                    time.sleep(10)
                    port = CONNECTION_OBJECT.get_connection()
            except Exception as e:
                error_message = 'Error in main loop'
                send_mail_or_logging(error_message, e)
    except Exception as e:
        error_message = 'Error in main loop'
        send_mail_or_logging(error_message, e)

    finally:
        CONNECTION_OBJECT.close_connection()

    threading.Thread(target=communicate_with_machine, daemon=True).start()

CONNECTION_OBJECT = Connection(
    com_port=COM_PORT,
    baudrate=BAUDRATE,
    timeout=TIMEOUT,
    report_file_path=REPORT_FILE_PATH,
    report_file_prefix=REPORT_FILE_PREFIX
)

port = CONNECTION_OBJECT.get_connection()


if __name__ == '__main__':
    try:
        threading.Thread(target=remove_old_logs_from_log_file,args=(LOG_FILE_LIST,) ,daemon=True).start()
        communicate_with_machine()

    except Exception as e:
        error_message = 'Error in main loop'
        send_mail_or_logging(error_message, e)
