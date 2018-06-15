class Constants(object):
    """description of class"""

    HOST = '127.0.0.1' 
    PORT = 8080

    SERVER_DIRECTORY = r'C:\Server File Storage'
    OUTPUT_FILE = 'output.xlsx'

    FILE_EXTENSION = '.xlsx'
    SERVER_FILE_NAME = 'test_upload' + FILE_EXTENSION
        
    File_EXT = ('.png', '.jpg', '.jpeg', '.txt', '.xlsx')
    ERROR_EXT = 'File extension not allowed.'

    SUCCESS_MESSAGE_BOTTLE ="(Bottle) File successfully saved to '{0}'."
    
    INPUT_SHEET1_NAME = 'Post 86 E&P and Tax Pools'
    INPUT_SHEET2_NAME = 'Pre 87 E&P and Tax Layers'

    COMPANY_SHEET1_START_CELL_NAME = 'B'
    COMPANY_SHEET2_START_CELL_NAME = 'C'

    COMPANY_SHEET1_START_CELL_INDEX = 18
    COMPANY_SHEET2_START_CELL_INDEX = 13

    DESCRIPTION_GENERAL = 'General Limitation Income'
    DESCRIPTION_PASSIVE = 'Passive Income'
    DESCRIPTION_OTHER = 'U.S. Income'

    EP_TAX_NAME_EP = 'ep'
    EP_TAX_NAME_TAX = 'tax'

    EP_TYPE_C3 = '959c3'
    EP_TYPE_C2 = '959c2'
    EP_TYPE_C1 = '959c1'

    TAX_TYPE_C3 = '959c3Tax'
    TAX_TYPE_C2 = '959c2Tax'
    TAX_TYPE_C1 = '959c1Tax'