from app import db
from datetime import datetime
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Product(UserMixin, db.Model):
    productname = db.Column(db.String(64))
    productprice = db.Column(db.Float)
    productdescription = db.Column(db.String(500))
    def __repr__(self):
        return f'<Product: {self.productname}>'

