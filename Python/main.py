from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return "Hello World"


@app.route('/double', methods=['GET'])
def double():
    query_val = int(request.args.get('value'))
    return f"Previous number was {query_val} the new value is {(query_val * 2)}"

if __name__ == '__main__':
    app.run(port=8080)