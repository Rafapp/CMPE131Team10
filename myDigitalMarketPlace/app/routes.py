from app import flaskObj
from flask import render_template

# Splash page (Umesh)
@flaskObj.route('splash')
def splash():
    return 'home'

# Home page (Rafael)
@flaskObj.route('/')
def home():
    return 'home'

# Log in (Rafael)
@flaskObj.route('login')
def login():
    return 'home'

# Sign up (Rafael)
@flaskObj.route('signup')
def signup():
    return 'home'

# Profile (Rafael)
@flaskObj.route('profile')
def profile():
    return 'home'

# Cart (Mohammad)
@flaskObj.route('cart')
def cart():
    return 'home'

# Item Search (Mohammad)
@flaskObj.route('itemsearch')
def itemearch():
    return 'home'

# Item seller (Umesh)
@flaskObj.route('seller')
def seller():
    return 'home'

# Item rating (Umesh)
@flaskObj.route('rating')
def cart():
    return 'home'