from flask_wtf import FlaskForm
from wtforms import FloatField,StringField, SubmitField, validators
from wtforms.validators import DataRequired

# Class for linking html to product database
class PostProductForm(FlaskForm):
  productname= StringField('Product Name' ,validators= [DataRequired(), validators.Length(max=64)])
  productprice=  FloatField('Product Price' ,  [DataRequired()])
  productdescription= StringField('Product Description' ,validators= [DataRequired(),validators.Length(max=500)])
  productimage = StringField('Image Link',validators = [validators.Length(max=500)])
  submit = SubmitField('Post')
  home = SubmitField('Home')

# Class for putting searches in the html
class SearchForm(FlaskForm):
  search = SubmitField('Search')
  searchbox = StringField("searchbox",validators = [DataRequired()])
 
# Class to add a product to the cart
class AddtoCartForm(FlaskForm):
   addtocart = SubmitField('Add to cart')