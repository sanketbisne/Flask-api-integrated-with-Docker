from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/about")
def aboutsection():
    return "this is about section"


@app.route("/resume")
def myresume():
    data = {
        'name': 'sanketbisne',
        'email': 'sanketbisne@gmail.com'
    }
    return jsonify(data)


if (__name__ == "__main__"):
    app.run(debug=True)
