from flask import Flask, jsonify
from flask_restful import request

app = Flask(__name__)

animals = [{'name': "Jerry", 'type': 'Mouse'},
           {'name': "Python", 'type': 'Snake'},
           {'name': "Tommy", 'type': 'Dog'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})
            
@app.route('/animal', methods=['GET'])
def getAll():
    return jsonify({'animals': animals})
            
@app.route('/animal/<string:name>', methods=['GET'])
def getOne(name):
    the_animal = [animal for animal in animals if animal['name'] == name]
    return jsonify({'animal': the_animal[0]})

@app.route('/animal', methods=['POST'])
def addOne():
    new_animal = {'name': request.json.get('name'), 'type': request.json.get('type')}
    animals.append(new_animal)
    return jsonify({'animals': animals})

@app.route('/animal/<string:name>', methods=['PUT'])
def editOne(name):
    the_animal = [animal for animal in animals if animal['name'] == name]
    the_animal[0]['name'] = request.json.get('name')
    return jsonify({'animal': the_animal[0]})

@app.route('/animal/<string:name>', methods=['DELETE'])
def deleteOne(name):
    the_animal = [animal for animal in animals if animal['name'] == name]
    animals.remove(the_animal[0])
    return jsonify({'animals': animals})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
