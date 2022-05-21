from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Model for a product posted in the catalogue (Mohammad)
class ProductModel(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  productname = db.Column(db.String(64),unique = False)
  productprice = db.Column(db.Float,unique = False)
  productdescription = db.Column(db.String(500),unique=False)
  productimage = db.Column(db.String(500),unique=False)
  #userid = db.Column(db.Integer(), db.ForeignKey('user_model.id'))

  def __repr__(self):
      return f'<Product: {self.productname}>'

# Model used for the cart system (Mohammad)
class CartModel(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  userid = db.Column(db.Integer(), db.ForeignKey('user_model.id'))
  #uid = db.Column(db.Integer,unique=False)
  productname = db.Column(db.String(64),unique = False)
  productprice = db.Column(db.Float,unique = False)
  productdescription = db.Column(db.String(500),unique=False)
  productimage = db.Column(db.String(500),unique=False)
  #itemid = db.Column(db.Integer(), db.ForeignKey('product_model.id'))

  def __repr__(self):
      return f'<Cart Product: {self.id}>'

# Model used for user accounts (Rafael)
class UserModel(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(64),unique = True)
  password_hash = db.Column(db.String(128))
  cart= db.relationship('CartModel',backref='author',lazy='dynamic')

  def set_password(self, password):
        self.password_hash = generate_password_hash(password)

  def check_password(self, password):
      return check_password_hash(self.password_hash, password)

  def __repr__(self):
    return f'<User: {self.email}>'

# Helper function to load a user given an ID
@login_manager.user_loader
def load_user(id):
   return UserModel.query.get(int(id))

# Model used for Rating ( Umesh )
class RateModel(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key = True)
  rating = db.Column(db.Integer)

  def __repr__(self):
      return f'<Rating: {self.rating}>'