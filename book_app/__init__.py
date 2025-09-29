from flask import Flask, jsonify, request, render_template
from config import Config

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

@app.route("/")
def hello():
    message = {"message": "Hellodd Flask API APP"}

    if request.headers.get("Accept") == "application/json":
        return jsonify(message)
    return render_template("index.html", data=message)

@app.route("/calculate", methods=['POST'])
def calculate():
    request_data = request.get_json()
    user_request = request_data['expression']
    result = eval(user_request)
    return jsonify({'response': result})
