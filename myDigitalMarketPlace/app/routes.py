from app import flaskObj
from flask import render_template

# Home page (Rafael)
@flaskObj.route('/')
def home():
    return render_template("Home.html")

# Log in (Rafael)
@flaskObj.route('/login')
def login():
    return render_template("Login.html")

# Sign up (Rafael)
@flaskObj.route('/signup')
def signup():
    return render_template("Signup.html")

# Profile (Rafael)
@flaskObj.route('/profile')
def profile():
    return render_template("Profile.html")

# Cart (Mohammad)
@flaskObj.route('/cart')
def cart():
    return 'cart'

# Item Search (Mohammad)
@flaskObj.route('/itemsearch')
def itemearch():
    return 'item search'

# Item seller (Umesh)
@flaskObj.route('/seller')
def seller():
    return 'seller'

# Item rating (Umesh)
@flaskObj.route('/rating')
def rating():
    return 'rating'

