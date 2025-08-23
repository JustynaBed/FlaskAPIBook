from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    message = {"message": "Hello Flask API APP"}

    if request.headers.get("Accept") == "application/json":
        return jsonify(message)
    return render_template("index.html", data=message)

@app.route("/calculate", methods=['POST'])
def calculate():
    request_data = request.get_json()
    user_request = request_data['expression']
    result = eval(user_request)
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=True)