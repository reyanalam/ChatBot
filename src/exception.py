import sys
from src.loggers import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Extract exception details
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where the exception occurred
    error_message = "Error occurred in python script name [{0}] Line number [{1}] Error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Get the line number and the error message
    )
    return error_message

class CustomeExceptionClass(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))  # Pass the string form of the error to the base class
        self.error_message = error_message_detail(error, error_detail=error_detail)  # Generate detailed error message
    
    def __str__(self):
        return self.error_message  # Return the custom error message when the exception is printed