from Helper import Helper
from Constants import Cons
from ReadExcel import ReadExcel


class FormMappingDS:

    qcat_form_template_id = ''
    sf_form_template_id = ''
    qcat_form_name = ''
    field_count = 0
    comment = ''
    file_name = ''

    qcat_item_names = {}
    qcat_item_values = {}
    sf_item_names = {}
    sf_item_values = {}

    def __init__(self):
        rx = ReadExcel()
        sheet = rx.Get_Sheet()

        '''load basic information'''
        self.qcat_form_template_id = sheet[Cons.EXCEL_QCAT_FORM_TEMPLATE_ID_CELL].value
        self.sf_form_template_id = sheet[Cons.EXCEL_SF_FORM_TEMPLATE_ID_CELL].value
        self.qcat_form_name = sheet[Cons.EXCEL_QCAT_FORM_NAME_CELL].value
        self.field_count = sheet[Cons.EXCEL_FIELD_COUNT_CELL].value
        self.comment = sheet[Cons.EXCEL_COMMENT_CELL].value
        self.file_name = sheet[Cons.EXCEL_FILE_NAME_CELL].value

        '''load item names with values'''
        self.load_form_mapping_items(sheet)
        Helper.print_all(self)

    def load_form_mapping_items(self, sheet):
        i = 0
        break_loop = 0

        for rowOfCellObjects in sheet[Cons.EXCEL_ITEM_START_CELL:Cons.EXCEL_ITEM_END_CELL]:
            i += 1
            if break_loop == 1:
                break

            for cellObj in rowOfCellObjects:
                if not cellObj.value:
                    break_loop = 1
                    break
                else:
                    if 'A' in cellObj.coordinate:
                        self.qcat_item_names[i] = cellObj.value
                    elif 'B' in cellObj.coordinate:
                        self.sf_item_names[i] = cellObj.value
                    elif 'C' in cellObj.coordinate:
                        self.qcat_item_values[i] = Helper.split_string_to_list(cellObj.value)
                    else:
                        self.sf_item_values[i] = Helper.split_string_to_list(cellObj.value)







