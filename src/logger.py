# logger.py

# This script sets up logging for the application, creating a log file with a timestamped filename
# in a 'logs' directory, and configuring the logging format and level.

import logging
import os
from datetime import datetime

# Generate a log file name based on the current datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path to the logs directory and the log file
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the logs directory if it doesn't already exist
os.makedirs(logs_path, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Set the log format
    level=logging.INFO,  # Set the logging level to INFO
)

# if __name__== '__main__':
#     logging.info('Logging has started')