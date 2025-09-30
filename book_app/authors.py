from flask import jsonify
from book_app import app

@app.route('/api/v1/authors', methods=['GET'])
def get_authors():
    return jsonify({
        'success': True,
        'data': 'Get all authors'
    })

@app.route('/api/v1/authors', methods=['POST'])
def create_author():
    return jsonify({
        'success': True,
        'data': 'New author has been created'
    }), 201