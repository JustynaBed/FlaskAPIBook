import json
from pathlib import Path
from sqlalchemy.sql import text
from datetime import datetime

from book_app import app, db
from book_app.models import Author

@app.cli.group()
def db_manage():
    """Database management commands"""
    pass

@db_manage.command()
def add_data():
    """Add sample data to database"""
    try:
        authors_path = Path(__file__).parent / 'samples' / 'authors.json'
        with open(authors_path) as file:
            data_json = json.load(file)
        for item in data_json:
            item['birth_date'] = datetime.strptime(item['birth_date'], '%d-%m-%Y').date()
            author = Author(**item)
            db.session.add(author)
        db.session.commit()
        print('Data has been successfully added to database')
    except Exception as exc:
        print('Unexpected error: {}'.format(exc))


@db_manage.command()
def remove_data():
    """Remove sample data to database"""
    try:
        query = text('TRUNCATE authors')
        db.session.execute(query)
        db.session.commit()
        print('Data has been successfully remove from database')
    except Exception as exc:
        print('Unexpected error: {}'.format(exc))