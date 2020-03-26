from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/about")
def aboutsection():
    return "this is about section"


@app.route("/best")
def myresume():
    data = [{
        'name': 'sanketbisne',
        'div': 'A,',
        'email': 'sanketbisne@gmail.com',
        'arr': [1, 2, 1, 45, 56]
    },
        {
        'name': 'netfix',
        'cloud': 'AWS',
        'SERVICES ': 'sagemaker',
        'music': 'spotify'
    }]
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
    app.run(host='0.0.0.0')
