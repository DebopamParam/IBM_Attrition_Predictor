import logging
import os
from datetime import datetime

# Generate the log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y__%Hh-%Mm-%Ss')}.log"

# Define the path for the logs directory
logs_dir = os.path.join(os.getcwd(), "logs")

# Ensure the logs directory exists
# exist_ok=True: If set to True, the function will not raise an error,
# if the directory specified by path already exists. Instead, it will simply do nothing and continue execution.
os.makedirs(logs_dir, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
