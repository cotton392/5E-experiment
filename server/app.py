from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy import desc
from flask import Blueprint, request, abort, jsonify, render_template
from datetime import datetime
from os.path import join, dirname
from dotenv import load_dotenv
import os
import ssl
import sys

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}'.format(**{
    'user': os.environ.get("DATABASE_USER"),
    'password': os.environ.get("DATABASE_PASSWORD"),
    'host': os.environ.get("DATABASE_HOST"),
    'port': 5432,
    'name': os.environ.get("DATABASE_NAME")
})

app = Flask(__name__)
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('server.crt', 'server.key')

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI


# ***************** database table definition *****************
class Menu(db.Model):
    """メニューの詳細情報テーブル"""
    __tablename__ = "cafeteria_menu_detail_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)  # Aセット・Bセット用
    menu_price = db.Column(db.Integer, nullable=False)
    is_sold_out = db.Column(db.Boolean, nullable=False, default=True)
    updated_at = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'menu_name': self.menu_name,
            'description': self.description,
            'menu_price': self.menu_price,
            'is_sold_out': self.is_sold_out,
            'updated_at': self.updated_at
        }


class Review(db.Model):
    """メニューのレビュー管理用テーブル"""
    __tablename__ = "cafeteria_review_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reviewed_menu = db.Column(db.String(255), nullable=False)
    review_detail = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.Integer, nullable=False)

    def __init__(self, reviewed_menu, review_detail, updated_at):
        self.reviewed_menu = reviewed_menu
        self.review_detail = review_detail
        self.updated_at = updated_at

    def to_dict(self):
        return {
            'id': self.id,
            'reviewed_menu': self.reviewed_menu,
            'review_detail': self.review_detail,
            'updated_at': self.updated_at
        }


db.create_all()


# ***************** api route *****************
@app.route('/api/get-menu', methods=['GET'])
def get_menu_detail():
    menus_detail = db.session.query(Menu).order_by(Menu.id).all()
    return jsonify({'menu_detail': [detail.to_dict() for detail in menus_detail]})


@app.route('/api/post-sell-condition', methods=['POST'])
def post_sell_condition():
    payload = request.json
    modified_menu_id = int(payload.get('modified_menu_id'))
    modified_menu = db.session.query(Menu).filter(Menu.id == modified_menu_id).first()
    print(modified_menu)
    modified_menu.is_sold_out = False

    db.session.add(modified_menu)
    db.session.commit()

    return jsonify(modified_menu.to_dict())


@app.route('/api/get-review', methods=['GET'])
def get_review_detail():
    db_res = db.session.query(Review).order_by(desc(Review.id)).limit(3)

    return jsonify({'reviews': [review.to_dict() for review in db_res]})


@app.route('/api/post-review', methods=['POST'])
def post_review_detail():
    payload = request.json
    reviewed_menu = payload.get('reviewed_menu')
    print(reviewed_menu)
    review_detail = payload.get('review_detail')
    updated_at = int(datetime.now().timestamp())

    review = Review(reviewed_menu, review_detail, updated_at)
    db.session.add(review)
    db.session.commit()

    return jsonify(review.to_dict())


# ***************** view route *****************
@app.route('/', methods=['GET'])
def index():
    return render_template("aaa.html")


# ***************** run app *****************
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]), ssl_context=context, debug=True)
