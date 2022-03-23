from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired


class PropertyForm(FlaskForm):
    property_title = StringField('Property Title', validators=[InputRequired()])
    bedrooms   = IntegerField('Number of Rooms', validators=[InputRequired()])
    bathrooms    = IntegerField('Number of Bathrooms', validators=[InputRequired()])
    location    = StringField('Location', validators=[InputRequired()])
    price       =  IntegerField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type', choices=[('house', 'House'), ('apartment', 'Apartment')])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo       = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])