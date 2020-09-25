from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "Hello World from Flask"

@app.route("/ping")
def pong():
    return "pong"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
