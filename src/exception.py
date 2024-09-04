import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name: [{0}] at line number : [{1}], Error_Message : {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):

    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
        logging.info(error_message)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 10
        b = 0
        c = a / b
    except Exception as e:
        exception = CustomException(e, sys)
        logging.info(exception)
        raise exception from e
