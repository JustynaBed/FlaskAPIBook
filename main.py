from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message": "Hello Flask API APP"})


@app.route("/calculate", methods=['POST'])
def calculate():
    request_data = request.get_json()
    user_request = request_data['expression']
    result = eval(user_request)
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=True)