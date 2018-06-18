import os
import json
from flask import Flask, jsonify
from flask_restful import request
from FileHelper import FileHelper
from ExceIO import ExceIO
from Constants import Constants as C
from paste import httpserver

app = Flask(__name__, static_folder=C.SERVER_DIRECTORY)
app.debug = True

@app.route('/upload/<operation>', methods=['POST'])
def upload(operation):
    try:
        file_handler = request.files.get('file')
        
        name, ext = os.path.splitext(file_handler.filename)
        if ext not in C.File_EXT:
            return C.ERROR_EXT
        
        fh = FileHelper()
        __filepath = fh.get_file_path(file_handler.filename)
        file_handler.save(__filepath)

        
        eio = ExceIO()
        eio.get_result(__filepath, operation)

        return C.SUCCESS_MESSAGE_FLASK.format(__filepath)

    except Exception as e:
        print(str(e))


@app.route('/download/<path:path>', methods=['GET'])
def download(path):
    try:
        return app.send_static_file(path)
        
    except Exception as e:
        print(str(e))

    
if __name__ == '__main__':
    app.run(debug=True, port=8080)
    