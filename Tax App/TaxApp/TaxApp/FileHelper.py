import os
import sys
import io
from io import BytesIO
import openpyxl
from Constants import Constants as C

class FileHelper(object):
    """description of class"""

    def __create_server_storage(self):
        try:
            if not os.path.exists(C.SERVER_DIRECTORY):
                os.makedirs(C.SERVER_DIRECTORY)
                print("Directory created successfully: {folder} ".format(folder=C.SERVER_DIRECTORY))
            return True

        except Exception as e:
            print(str(e))
            return False

    def get_file_path(self, filepath):
        if self.__create_server_storage() == True:
            try:
                __filepath = os.path.join(C.SERVER_DIRECTORY, filepath)
                return __filepath

            except Exception as e:
                print(str(e))
                return ''

    def save_workbook(self, contents):
        try:
            filepath = self.get_file_path(C.DOWNLOAD_FILE_NAME)
            
            if filepath != '':
                wb = openpyxl.load_workbook(filename=BytesIO(contents))
                wb.save(filepath)
                print(C.SUCCESS_MESSAGE)

        except Exception as e:
            print(str(e))


