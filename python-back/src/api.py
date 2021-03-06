import flask
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/test', methods=['GET'])
def ok():
    return '{ "status":"ok"}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

