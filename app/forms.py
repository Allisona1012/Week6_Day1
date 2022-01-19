from re import L
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Email 

class RegisterForm(FlaskForm):
    full_name= StringField('Full name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    phone_number= StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Submit')
