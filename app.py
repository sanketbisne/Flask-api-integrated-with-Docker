from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/about")
def aboutsection():
    return "this is about section"


def myresume():
    data = {
        'name': 'sanketbisne',
        'email': 'sanketbisne@gmail.com'
    }
    return jsonify(data)


@app.route('/add_two_numbers', methods=["POST"])
def add_two_nums():
    dataDictt = request.get_json()
    x = dataDictt["x"]
    y = dataDictt["y"]
    z = x+y

    retJSON = {
        "z": z
    }
    return jsonify(retJSON), 200
# 200 = Success
# 500 = NOT FOUND


if (__name__ == "__main__"):
    app.run()
