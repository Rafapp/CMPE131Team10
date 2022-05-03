from app import myapp_obj

from flask import render_template, flash, request

from flask_wtf import FlaskForm

from wtforms import FloatField,StringField, IntegerField, BooleanField, SubmitField, validators
 
from wtforms.validators import InputRequired, DataRequired, Length


from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required


class PostProduct(FlaskForm):
	productname= StringField('Product Name' ,validators= [DataRequired(), validators.Length(max=64)])
	productprice=  FloatField('Product Price' ,  [DataRequired()])
	productdescription= StringField('Product Description' ,validators= [DataRequired(),validators.Length(max=500)])
	submit = SubmitField('Post')
@myapp_obj.route('/PostProduct',methods=['GET','POST'])
def Product():
	form= PostProduct()
	if request.method == 'POST' and form.validate():
                product = Product(form.productname.data, form.productprice.data, form.productdescription.data)
               	db_session.add(user)
                result= 'Your item has been posted'
                flash('Your item has been posted')
                return render_template('ListItemForSelling.html', form=form,result=result)
	if request.method == 'GET' and form.validate():
		return render_template('ListItemForSelling.html', form=form)
	else:
		return render_template('ListItemForSelling.html', form=form)
