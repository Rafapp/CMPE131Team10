from app import flaskObj
from flask import render_template

from sqlalchemy.orm import Session
from flask import  flash,request, redirect
 
from flask_wtf import FlaskForm
 
from wtforms import FloatField,StringField, IntegerField, BooleanField, SubmitField, validators
from wtforms.validators import InputRequired, DataRequired, Length
from app import db
from app.models import Product1, Cart
 
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
 
db.create_all()

class PostProduct(FlaskForm):
   productname= StringField('Product Name' ,validators= [DataRequired(), validators.Length(max=64)])
   productprice=  FloatField('Product Price' ,  [DataRequired()])
   productdescription= StringField('Product Description' ,validators= [DataRequired(),validators.Length(max=500)])
   productimage = StringField('Image Link',validators = [validators.Length(max=500)])
   submit = SubmitField('Post')
   home = SubmitField('Home')
  
 
class SearchClass(FlaskForm):
   search = SubmitField('Search')
   searchbox = StringField("searchbox",validators = [DataRequired()])

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

@flaskObj.route('/hometest',methods=['GET','POST'])
def Home():
   form=SearchClass()
   if request.method == 'GET':
       return render_template('hometest.html', form=form)
   if request.method == 'POST':
       return redirect('/search')

@flaskObj.route('/inbetween',methods=['GET','POST'])
def inbetween():
   form= PostProduct()
   if request.method == 'GET':
       submit = SubmitField('Home')
       return render_template('inbetween.html', home=submit,form=form)
   if request.method == 'POST':
       return redirect('/hometest')

@flaskObj.route('/search',methods=['GET','POST'])
def searchresult():
   form= SearchClass()
   list = []
   searchedphrase = Product1.query.all()
   if form.validate_on_submit():
   #if request.method == 'POST':
       result = request.form['searchbox']
       product = Product1.query.filter(Product1.productname == result).first()
       #searchedphrase = Product1.query.filter_by(productname = result).first()
       for i in searchedphrase:
           if (i.productname==result):
              
               list.append(i.productname)
      
       return render_template('search.html',result=result,form=form,searchedphrase=searchedphrase,product=product,list=list)
       #return redirect('/searchhelp')
   return render_template('search.html',form=form,)
   #if request.method == 'POST':
       #return redirect('/home')


@flaskObj.route('/PostProduct',methods=['GET','POST'])
def Product():
   form= PostProduct()
   #if request.method == 'POST':
               #product = Product1(productname=form.productname.data,productprice= form.productprice.data,productdescription= form.productdescription.data,productimage=form.productimage.data)
               #db.session.add(product)
               #db.session.commit()
               #result= 'Your item has been posted'
               #flash(result)
               #return redirect('/home')
   if request.method == 'GET':
       return render_template('ListItemForSelling.html', form=form)
   if request.method == 'POST':
       product = Product1(productname=form.productname.data,productprice= form.productprice.data,productdescription= form.productdescription.data,productimage=form.productimage.data)
       db.session.add(product)
       db.session.commit()
       return redirect('/inbetween')




