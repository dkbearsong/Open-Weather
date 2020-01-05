from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class FindWeatherForm(FlaskForm):
  city = StringField('City', validators=[DataRequired(), Length(min=2, max=30)])
  state = StringField('State/Province', validators=[DataRequired(), Length(min=2, max=30)])
  country = StringField('Country', validators=[DataRequired(), Length(min=2, max=30)])
  submit = SubmitField('Submit')      