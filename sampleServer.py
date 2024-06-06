from flask import Flask, jsonify

app = Flask(__name__)

# Flask app = new Flask(8080, true);

@app.route('/hello')
def hello_world():
    response_data = {
        'msg': 'Hello, World!'
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(port = 8080, debug = False)