from app import models, db, flaskObj, forms
from flask import  flash, request, redirect, render_template
from flask_login import current_user, login_user, logout_user, login_required

# Create the database to manage the data
db.create_all()

# Search page (Rafael)
@flaskObj.route('/')
def Home():
    return render_template("Home.html")

# Log in (Rafael)
@flaskObj.route('/login', methods = ['GET', 'POST'])
def login():
    loginForm = forms.LoginForm()
    email = loginForm.email.data
    password = loginForm.password.data
    if loginForm.validate():
        # We try to find a matching email and password in the database
        user = models.UserModel.query.filter_by(email = str(email)).first()
        if not user or not models.UserModel.check_password(user, password):
            flash('Your password was incorrect, or the account does not exist. Please try again.')
            return redirect('/login')
        login_user(user)
        return 'Logged in successfully, you may return to the home page'
    return render_template("Login.html", form = loginForm)

# Sign up (Rafael)
@flaskObj.route('/signup', methods = ['GET', 'POST'])
def signup():
    signupForm = forms.SignUpForm()
    if request.method == 'POST' and signupForm.validate():
        email = signupForm.email.data
        password = signupForm.password.data
        user = models.UserModel(email = email, password_hash = password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return 'Created account succesfully! Please log in :)'
    return render_template("Signup.html", form = signupForm)

# Profile (Rafael)
@login_required
@flaskObj.route('/profile')
def profile():
    return render_template("Profile.html")

# Deleted account (Rafael)
@flaskObj.route('/deleteaccount')
def deleteaccount():
    models.User.query.delete()
    return 'Account succesfully deleted'

# Cart (Mohammad)
@login_required
@flaskObj.route('/cart')
def cart():
    # Adds whatever is pressed on to the Cart database
    product_id = request.form.get('product_id')
    product= Product.query.filter_by(id=product_id).first()
    if request.method =="POST":
        u = models.CartModel(productname= product.productname, productprice = product.productprice, productimage = product.productimage)
        db.session.add(u)
        db.session.commit()
    return render_template('cart.html')
 
# Post product success (Mohammad)
@login_required
@flaskObj.route('/postProductSuccess',methods=['GET','POST'])
def postProductSuccess():
    #Confirms to customer that their product has been posted then allows them to go to Search
    form = forms.PostProductForm()
    if request.method == 'GET':
        submit = forms.SubmitField('Home')
        return render_template('PostedProductSuccess.html', home = submit,form = form)
    if request.method == 'POST':
        return redirect('/')

# Item gallery (Mohammad)
@flaskObj.route('/itemgallery',methods=['GET','POST'])
def Gallery():
  form = forms.SearchForm()
  if request.method == 'GET':
      return render_template('ItemGallery.html', form=form)
  if request.method == 'POST':
      return redirect('/search')

# Item Search (Mohammad)
@flaskObj.route('/search',methods=['GET','POST'])
def SearchItem():
    #When search is clicked, the searched phrase is compared to the products database to display all matches
    form = forms.SearchForm()
    cart = forms.AddtoCartForm()
    productList = []
    searchedphrase = models.ProductModel.query.all()

    if form.validate_on_submit():
        result = request.form['searchbox']
        product = models.ProductModel.query.filter(models.ProductModel.productname == result).first()

    for i in searchedphrase:
        if (i.productname == result):
            productList.append(i.productname)

        return render_template('Search.html', result=result,form=form, searchedphrase=searchedphrase, product=product, productList=productList, cart=cart)

    return render_template('Search.html', form = form)

# Post product page (Mohammad)
@login_required
@flaskObj.route('/PostProduct', methods=['GET','POST'])
def Product():
  #Saves whatever is inputed into the products databse
  form = forms.PostProductForm()
  if request.method == 'GET':
      return render_template('ListItemForSelling.html', form=form)
  if request.method == 'POST':
      product = models.ProductModel(productname = form.productname.data, productprice = form.productprice.data, productdescription = form.productdescription.data, productimage = form.productimage.data)
      db.session.add(product)
      db.session.commit()
      return redirect('/postProductSuccess')

# Item seller (Umesh)
@login_required
@flaskObj.route('/seller')
def seller():
    return 'seller'

# Item rating (Umesh)
@login_required
@flaskObj.route('/rating')
def rating():
    return render_template('RateItem.html')

