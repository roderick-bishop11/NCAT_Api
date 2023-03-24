from flask import *
import repo, simpleService

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return "Hello World"


@app.route('/HBCU', methods=['GET'])
def getOneCollege():
    name = request.args.get('name') or None
    print(name)
    if name is None:
        return repo.findAll()
    else:
        return repo.findOne(name)


@app.route('/HBCU', methods=['POST'])
def postOneCollege():
    newCollege = request.json
    resp = repo.addOne(newCollege)
    return resp


@app.route('/HBCU', methods=['DELETE'])
def deleteOneCollege():
    deletedCollege = request.json
    resp = repo.deleteOne(deletedCollege)
    return resp

@app.route('/HBCU', methods=['PATCH'])
def patchOneCollege():
    patch = request.json
    resp = repo.patchOne(patch)
    return resp

def postOneWithoutSpaces():
    newCollege = request.json
    resp = simpleService.addWithoutSpaces(newCollege)
    return resp

if __name__ == '__main__':
    app.run(port=8080)
