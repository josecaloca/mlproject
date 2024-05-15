import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed error message including the script name, line number, and error message.

    Args:
    - error: The error/exception object.
    - error_detail: The sys module to extract exception details.

    Returns:
    - A formatted error message string.
    """
    # Extract exception traceback information
    _, _, exc_tb = error_detail.exc_info()
    # Get the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Format the error message with script name, line number, and error message
    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    
    return error_message

class CustomException(Exception):
    """
    Custom Exception class for handling and logging detailed errors.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the CustomException with a detailed error message.

        Args:
        - error_message: The error message.
        - error_detail: The sys module to extract exception details.
        """
        super().__init__(error_message)
        # Get the detailed error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        """
        Returns the detailed error message when the exception is printed.
        """
        return self.error_message

# if __name__== '__main__':
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e, sys)