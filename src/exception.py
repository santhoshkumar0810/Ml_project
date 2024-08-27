import sys
import logging

def error_message_detail(error: Exception, error_detail:sys) -> str:
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
            f" Error occured in python script name [ {file_name} ] "
            f"Line number [{exc_tb.tb_lineno}] "
            f"error message [ {str(error)} ] "
            )
   
    return error_message


class CustomException(Exception):

    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message


