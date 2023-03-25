from flask import *
import repo

app = Flask(__name__)


# base route
@app.route('/', methods=['GET'])
def home_page():
    return "Hello World"


@app.route('/HBCU', methods=['GET'])
def getOneCollege():
    name = request.args.get('name') or None
    if name is None:
        return repo.findAll()
    else:
        return repo.findOne(name)


@app.route('/HBCU', methods=['POST'])
def postOneCollege():
    newCollege = request.json
    response = repo.addOne(newCollege)
    return response


@app.route('/HBCU', methods=['DELETE'])
def deleteOneCollege():
    deletedCollege = request.json
    response = repo.deleteOne(deletedCollege)
    return response


@app.route('/HBCU', methods=['PUT'])
def patchOneCollege():
    patch = request.json
    response = repo.putOne(patch)
    return response


if __name__ == '__main__':
    app.run(port=8080)
