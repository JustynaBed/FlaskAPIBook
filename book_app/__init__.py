from flask import Flask, jsonify, request, render_template, send_from_directory
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")
# app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# with app.app_context():
#     results = db.session.execute(text('show databases'))
# for row in results:
#     print(row)

from book_app import authors
from book_app import models
from book_app import db_manage_commands
# from book_app.models import Author, AuthorSchema

@app.route("/")
def hello():
    # authors = Author.query.all()
    # author_schema = AuthorSchema(many=True)
    # authors_data = author_schema.dump(authors)

    message = {"message": "Hello Flask API APP"}

    if request.headers.get("Accept") == "application/json":
        return jsonify(message)

    return send_from_directory(app.static_folder, "index.html")