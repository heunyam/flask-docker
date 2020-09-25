from flask import Flask


app = Flask(__name__)


@app.route("/flask2")
def hello_flask2():
    return "<h1>Hello Flaskapp2</h1>"

@app.route("/ping2")
def pong():
    return "pong"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
