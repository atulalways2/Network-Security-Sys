import os
import sys
from networksecurity.logging.logger import logger


class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)

        self.error_message = error_message

        _, _, exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (
            "Error occured in python script name [{0}] "
            "line number [{1}] "
            "error message [{2}]"
        ).format(
            self.file_name,
            self.lineno,
            str(self.error_message)
        )

    # def __init__(self,error_message,error_details:sys):
    #     self.error_message = error_message
    #     _,_,exc_tb = error_details.exc_info()       # returns three type of value--> exception type,exception value,exception traceback object;we only require the traceback object
        
    #     self.lineno=exc_tb.tb_lineno
    #     self.file__name=exc_tb.tb_frame.f_code.co_filename      # filename error now has -> error object,frame(what was it executing while the error happend),f_code=the code object,and the file name which caused the error


    # def __str__(self):
    #         return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    #     self.file_name.self.lineno,str(self.error_message))


"""Below code serves as the test-case for exception code"""
# if __name__=='__main__':
#     try:
#         logger.info("Entered the try block..")
#         a=1/0
#         print("this will no be printed as this is an undefined expression",a)
#     except Exception as e:
#         logger.info("try block excution failed entered exnetworkception")
#         raise NetworkSecurityException(e,sys)
