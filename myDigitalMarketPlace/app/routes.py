from app import flaskObj
from flask import render_template
from flask import  flash,request, redirect
from flask_wtf import FlaskForm
from wtforms import FloatField,StringField, BooleanField, SubmitField, validators, PasswordField
from wtforms.validators import DataRequired
from app import db
from app.models import Product1, Cart
from app import models

# Create the database to manage the data
db.create_all()

# Class for linking html to product database
class PostProduct(FlaskForm):
  productname= StringField('Product Name' ,validators= [DataRequired(), validators.Length(max=64)])
  productprice=  FloatField('Product Price' ,  [DataRequired()])
  productdescription= StringField('Product Description' ,validators= [DataRequired(),validators.Length(max=500)])
  productimage = StringField('Image Link',validators = [validators.Length(max=500)])
  submit = SubmitField('Post')
  home = SubmitField('Home')

# Class for putting searches in the html
class SearchClass(FlaskForm):
  search = SubmitField('Search')
  searchbox = StringField("searchbox",validators = [DataRequired()])
 
# Class to add a product to the cart
class AddtoCart(FlaskForm):
   addtocart = SubmitField('Add to cart')


# Home page (Rafael)
@flaskObj.route('/')
def home():
    return render_template("Home.html")

# Log in (Rafael)
@flaskObj.route('/login')
def login():
    current_form = LoginForm()
    if current_form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}' .format(current_form.username.data, current_form.remember_me.data))
        return redirect('/')
    return render_template("Login.html", title='Sign in', form=current_form)

# Sign up (Rafael)
@flaskObj.route('/signup')
def signup():
    return render_template("Signup.html")

# Profile (Rafael)
@flaskObj.route('/profile')
def profile():
    return render_template("Profile.html")

# Cart (Mohammad)
# adds whatever is pressed on to the Cart database
@flaskObj.route('/cart')
def cart():
   product_id = request.form.get('product_id')
   product= Product1.query.filter_by(id=product_id).first()
   if request.method =="POST":
       u = Cart(productname= product.productname, productprice = product.productprice, productimage=product.productimage)
       db.session.add(u)
       db.session.commit()
   return render_template('cart.html')

# Item Search (Mohammad)
 
#Confirms to customer that their product has been posted then allows them to go to home
@flaskObj.route('/inbetween',methods=['GET','POST'])
def inbetween():
  form= PostProduct()
  if request.method == 'GET':
      submit = SubmitField('Home')
      return render_template('inbetween.html', home=submit,form=form)
  if request.method == 'POST':
      return redirect('/')

@flaskObj.route('/itemgallery',methods=['GET','POST'])
def Home():
  form=SearchClass()
  if request.method == 'GET':
      return render_template('itemgallery.html', form=form)
  if request.method == 'POST':
      return redirect('/search')

#When search is clickled, the searched phrase is compared to the products database to display all matches
@flaskObj.route('/search',methods=['GET','POST'])
def searchresult():
    form= SearchClass()
    cart= AddtoCart()
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
        return render_template('search.html',result=result,form=form,searchedphrase=searchedphrase,product=product,list=list,cart=cart)
    #return redirect('/searchhelp')
    return render_template('search.html',form=form,)

#Saves whatever is inputed into the products databse
@flaskObj.route('/PostProduct',methods=['GET','POST'])
def Product():
  form= PostProduct()
  if request.method == 'GET':
      return render_template('ListItemForSelling.html', form=form)
  if request.method == 'POST':
      product = Product1(productname=form.productname.data,productprice= form.productprice.data,productdescription= form.productdescription.data,productimage=form.productimage.data)
      db.session.add(product)
      db.session.commit()
      return redirect('/inbetween')


# Item seller (Umesh)
@flaskObj.route('/seller')
def seller():
    return 'seller'

# Item seller (Umesh)
@flaskObj.route('/deleteaccount')
def deleteaccount():
    models.User.query.delete()
    return 'Account succesfully deleted'

# Item rating (Umesh)
@flaskObj.route('/rating')
def rating():
    return render_template('RateItem.html')

