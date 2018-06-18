import os
import json
import bottle
from bottle import static_file 
from FileHelper import FileHelper
from ExcelRW import ExcelRW
from Constants import Constants as C
from paste import httpserver

@bottle.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    bottle.response.headers['Access-Control-Allow-Origin']  = '*'
    bottle.response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    #bottle.response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@bottle.route('/upload', method='POST')
def upload():
    try:
        file_handler = bottle.request.files.get('file')
        
        name, ext = os.path.splitext(file_handler.filename)
        if ext not in C.File_EXT:
            return C.ERROR_EXT
        
        fh = FileHelper()
        __filepath = fh.get_file_path(file_handler.filename)
        file_handler.save(__filepath)
        
        e_rw = ExcelRW()
        e_rw.get_result(__filepath)

        return C.SUCCESS_MESSAGE_BOTTLE.format(__filepath)

    except Exception as e:
        print(str(e))


@bottle.route('/download/<filename:path>', method='GET')
def download(filename):
    try:
        return static_file(filename, root=C.SERVER_DIRECTORY, download=filename)
        
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    bottle.run(host=C.HOST, port=C.PORT, debug=True)
    
    '''
    application = bottle.default_app()
    httpserver.serve(application, host='0.0.0.0', port=8080)
    '''
    
