import os
import logging
import time
import datetime
import serial # type: ignore
import smtplib
import threading
from email.message import EmailMessage

connection_type = 'tty'
input_tty = 'COM4'
s = None
x = None
output_folder = 'C:\\ASTM\\root\\report_file\\'
log_file = 'C:\\ASTM\\root\\log_file\\logging_for_aia_360_info.log'
error_log_file = 'C:\\ASTM\\root\\log_file\\loggin_for_aia_360_error.log'
disconnect_interval = 86400  # 1 day
log_retention_hours = 48  # 2 days
log_check_interval = 86400  # 24 hours (in seconds)

# subject = "Email From Apex Hospital"
# to_email = "lishealthray@gmail.com"
# from_email = "kaushikjasoliya6@gmail.com"
# password = "kzen iwrq mkhi ueio"  

# def send_email(subject, body, to_email, from_email, password):
#     try:
#         # Create the email message
#         msg = EmailMessage()
#         msg['Subject'] = subject
#         msg['From'] = from_email
#         msg['To'] = to_email
#         msg.set_content(body)

#         # Connect to Gmail SMTP server
#         with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#             smtp.ehlo()
#             smtp.starttls()  # Secure the connection
#             smtp.login(from_email, password)
#             smtp.send_message(msg)

#         logger.info("Email sent successfully!")
#         return True
#     except Exception as e:
#         logger.error(f"Failed to send email: {e}")
#         return False

def setup_loggers():
    """Set up separate loggers for info and error."""
    try:
        logger = logging.getLogger("app_logger")
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
        error_message = 'Error in LOG file initialize'
        send_mail_or_logging(error_message, e)

# log = setup_loggers()
logger = setup_loggers()

logger.info("Log file initialized.")
logger.error("Error Log file initialized.")

log_file_list = [log_file, error_log_file]

def send_mail_or_logging(error_message, error, file_name):
    logger.error(f'{error_message} : {error}')
    body_for_email = (f'{error_message} \n {error}')
    # is_send_mail = send_email(subject, body_for_email, to_email, from_email, password)
    # if not is_send_mail:
    #     try:
    #         log_data = [f'{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', file_name, error_message, error]
    #         # sheet_log.append_row(log_data)
    #     except Exception as e:
    #         logger.error(f"Error in append data in sheet :- {e}")

def manage_log_file(log_file_list):
    """Deletes the log file if it's older than 48 hours and creates a new one."""
    try:
      while True:
          for file in log_file_list:
            if os.path.exists(file):
                file_age = time.time() - os.path.getmtime(log_file)  # File age in seconds
                if file_age > log_retention_hours * 3600:  # Convert hours to seconds
                    os.remove(log_file)
                    logger.info(f"Deleted old log file: {log_file}")         

          time.sleep(log_check_interval)
    except Exception as e:
        error_message = 'Error in LOG file'
        send_mail_or_logging(error_message, e)


def get_filename():
    try:
      dt = datetime.datetime.now()
      return output_folder + 'aia_360_' + dt.strftime("%Y-%m-%d-%H-%M-%S-%f")
    except Exception as e:
        error_message = 'Error in get_filename'
        send_mail_or_logging(error_message, e)

def get_port():
    try:
        port = serial.Serial(port=input_tty, baudrate=9600, timeout=1)
        return port
    except serial.SerialException as se:
        error_message = 'Error in Connection'
        send_mail_or_logging(error_message, se)

def my_read(port):
    try:
        data = port.read(1)
        return data
    except Exception as e:
        error_message = 'Error in Reading data from port'
        send_mail_or_logging(error_message, e)

def my_write(port, byte):
    try:
        port.write(byte)
        # print(byte)
    except Exception as e:
        error_message = 'Error in writing data to port'
        send_mail_or_logging(error_message, e)

port = get_port()



cur_file = None
byte_array = []
last_two_chars = []

try:
    while True:
        try:
            if port:
                byte = my_read(port)
                if byte:
                    char = chr(ord(byte))
                    byte_array.append(char)
                    last_two_chars.append(char) 
                     
                    # Maintain last 2 characters                        
                    if len(last_two_chars) > 2:
                        last_two_chars.pop(0)

                    # Check for end of message: '\r\n'
                    if last_two_chars == ['\r', '\n']:  
                        print(byte_array)
                        print("Message complete. Writing to file...")
                        print("Message content:", ''.join(byte_array))
                        cur_file = get_filename()
                        try:
                            with open(cur_file, 'w') as f:
                                f.write(''.join(byte_array))
                            print(f"File Saved & Closed: {cur_file}")
                        except IOError as ioe:
                            error_message = 'Error in txt file initialize'
                            send_mail_or_logging(error_message, ioe)
                        byte_array = []
                        last_two_chars = []

            else:
                time.sleep(10)
                port = get_port()
                
        except Exception as e:
            error_message = 'Error in main loop'
            send_mail_or_logging(error_message, e)
except Exception as e:
    error_message = 'Error in main loop'
    send_mail_or_logging(error_message, e)