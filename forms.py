from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError
import re

class account(FlaskForm):
    # user name not null and not too long. Add validation
    username = StringField("Username", validators=[DataRequired(), Length(min = 2, max = 30)])
    email = StringField("Email", validators=[DataRequired(), Length(min = 6)])

    def tamu_email_validate(self, form, field):
        # [A-Za-z0-9] firt character to match it.
        if not re.search(r"^[A-Za-z0-9](\.?[a-z0-9]){5,}@tamu\.edu$", field.data):
            raise ValidationError("Invalid Email Address")
        return True

    # password =

