class Constants(object):
    """description of class"""

    HOST = '127.0.0.1' 
    PORT = 8080

    SERVER_DIRECTORY = r'C:\Server File Storage'
    
    FILE_EXTENSION = '.xlsx'
    SERVER_FILE_NAME = 'test_upload' + FILE_EXTENSION
        
    File_EXT = ('.png', '.jpg', '.jpeg', '.txt', '.xlsx')
    ERROR_EXT = 'File extension not allowed.'

    SUCCESS_MESSAGE_BOTTLE ="(Bottle) File successfully saved to '{0}'."
    SUCCESS_MESSAGE_FLASK ="(FLASK) File successfully saved to '{0}'."