from Constants import Cons
import openpyxl


class ReadExcel:

    def Get_Sheet(self):

        wb = openpyxl.load_workbook(Cons.FILE_PATH)
        sheet = wb.get_sheet_by_name('Sheet1')

        return sheet



