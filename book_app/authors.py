from flask import jsonify, request
from book_app import app, db
from book_app.models import Author, AuthorSchema, author_schema
from datetime import datetime

@app.route('/api/v1/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    author_schema = AuthorSchema(many=True)

    return jsonify({
        'success': True,
        'data': author_schema.dump(authors),
        'number_of_records':len(authors)
    })

@app.route('/api/v1/authors/<int:author_id>', methods=['GET'])
def get_author(author_id: int):
    author = Author.query.get_or_404(author_id, description=f'Author with id {author_id} not found')

    return jsonify({
        'success': True,
        'data': author_schema.dump(author)
    })

@app.route('/api/v1/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    birth_date_str = data.get('birth_date')
    birth_date = datetime.strptime(birth_date_str, '%d-%m-%Y').date()
    author = Author(first_name=first_name, last_name=last_name, birth_date=birth_date)

    db.session.add(author)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': 'New author has been created'
    }), 201

@app.route('/api/v1/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    data = request.json
    author = Author.query.get(author_id)

    author.first_name = data.get('first_name', author.first_name)
    author.last_name = data.get('last_name', author.last_name)
    birth_date_str = data.get('birth_date')

    if birth_date_str:
        author.birth_date = datetime.strptime(birth_date_str, '%d-%m-%Y').date()

    db.session.commit()

    return jsonify({
        'success': True,
        'data': f"Author with id {author_id} has been updated"
    })

@app.route('/api/v1/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id: int):
    author = Author.query.get_or_404(author_id, description=f'Author with id {author_id} not found')

    db.session.delete(author)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': f'Author with id {author_id} has been deleted'
    })