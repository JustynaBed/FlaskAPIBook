from flask import Flask, jsonify, request, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

db = SQLAlchemy(app)

# with app.app_context():
#     results = db.session.execute(text('show databases'))
# for row in results:
#     print(row)

from book_app import authors
from book_app import models

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
