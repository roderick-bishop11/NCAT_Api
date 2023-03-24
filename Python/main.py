from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return "Hello World"


@app.route('/double', methods=['POST'])
def double():
    query_val = request.json['value']
    return f"Previous number was {query_val} the new value is {(int(query_val) * 2)}"


if __name__ == '__main__':
    app.run(port=8080)
