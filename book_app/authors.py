from flask import jsonify, request
from webargs.flaskparser import use_args
from book_app import app, db
from book_app.models import Author, AuthorSchema, author_schema


@app.route('/api/v1/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    author_schema = AuthorSchema(many=True)

    return jsonify({
        'success': True,
        'data': author_schema.dump(authors),
        'number_of_records':len(authors)
    })

@app.route('/api/v1/authors', methods=['POST'])
@use_args(author_schema)
def create_author(args: dict):
    author = Author(**args)

    db.session.add(author)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': author_schema.dump(author)
    }), 201