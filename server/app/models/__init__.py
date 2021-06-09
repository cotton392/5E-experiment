from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init():
    db.create_all()