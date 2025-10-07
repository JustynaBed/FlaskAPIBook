from book_app import app, db

@app.cli.group()
def db_manage():
    """Database management commands"""
    pass

@db_manage.command()
def add_date():
    """Add sample data to database"""
    pass

@db_manage.command()
def remove_date():
    """Remove sample data to database"""
    pass