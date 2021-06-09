import dotenv
from sqlalchemy import Column, Integer, String, DateTime
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': '',
    'password': '',
    'host': '',
    'name': 'db.postgresql'
})

DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY")