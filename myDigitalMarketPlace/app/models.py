from app import db
from flask_login import UserMixin

class ProductModel(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  productname = db.Column(db.String(64),unique = False)
  productprice = db.Column(db.Float,unique = False)
  productdescription = db.Column(db.String(500),unique=False)
  productimage = db.Column(db.String(500),unique=False)
  def __repr__(self):
      return f'<Product: {self.productname}>'

class CartModel(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  productname = db.Column(db.String(64),unique = False)
  productprice = db.Column(db.Float,unique = False)
  productimage = db.Column(db.String(500),unique=False)
  def __repr__(self):
      return f'<Product: {self.productname}>'
