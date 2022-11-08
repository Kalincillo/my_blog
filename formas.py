from flask_wtf import FlaskForm, recaptcha
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf.recaptcha import RecaptchaField

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField(
        'name',
        [DataRequired()]
    )
    email = StringField(
        'Email',
        [
            Email(message=('Not a valid email address.')),
            DataRequired()
        ]
    )
    body = StringField(
        'Message',
        [
            DataRequired(),
            Length(min=4,
                   message=('Your message is too short.'))
        ]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
