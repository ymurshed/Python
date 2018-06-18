from bottle import run, get, post, delete, request
import bottle

animals = [{'name': "Ellie", 'type': 'Elephant'},
           {'name': "Python", 'type': 'Snake'},
           {'name': "Zed", 'type': 'Zebra'}]

@bottle.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    bottle.response.headers['Access-Control-Allow-Origin']  = '*'
    bottle.response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    #bottle.response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    
@get('/animal')
def getAll():
    return {'animals' : animals}

@get('/animal/<name>')
def getOne(name):
    the_animal = [animal for animal in animals if animal['name'] == name]
    return {'animal': the_animal[0]}

@post('/animal')
def addOne():
    new_animal = {'name': request.json.get('name'), 'type': request.json.get('type')}
    animals.append(new_animal)
    return {'animals': animals}

@delete('/animal/<name>')
def removeOne(name):
    the_animal = [animal for animal in animals if animal['name'] == name]
    animals.remove(the_animal[0])

run(reloader=True, debug=True)