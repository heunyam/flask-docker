from flask import Flask


app = Flask(__name__)


@app.route("/flask2")
def flask2():
    return "<h1>Hello Flaskapp2</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
