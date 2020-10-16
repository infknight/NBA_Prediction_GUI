from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class account(FlaskForm):
    # user name not null and not too long. Add validation
    username = StringField("Username", validators=[DataRequired(), Length(min = 2, max = 30)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min = 6)])
    # password =

