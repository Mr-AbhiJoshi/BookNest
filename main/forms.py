from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, TextAreaField, SelectField, ValidationError
from wtforms.validators import Length, Email, EqualTo, DataRequired, Optional, NumberRange
from main.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username.')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address.')

    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1', message='The passwords entered do not match. Please enter both passwords carefully.'), DataRequired()])
    submit = SubmitField(label='Create Account')
    
class LoginForm(FlaskForm):
	username = StringField(label='Username:', validators=[DataRequired()])
	password = PasswordField(label='Password:', validators=[DataRequired()])
	submit = SubmitField(label='Sign in')

class EditProfileForm(FlaskForm):
    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    bio = TextAreaField(label='Bio:', validators=[Length(max=500)])
    
    icon = SelectField('Profile Icon', choices=[
        ('static/user/default.jpg', 'Default'),
        ('static/user/icon1.jpg', 'Icon 1'),
        ('static/user/icon2.jpg', 'Icon 2'),
        ('static/user/icon3.jpg', 'Icon 3'),
        ('static/user/icon4.jpg', 'Icon 4'),
        ('static/user/icon5.jpg', 'Icon 5'),
        ('static/user/icon6.jpg', 'Icon 6'),
        ('static/user/icon7.jpg', 'Icon 7'),
        ('static/user/icon8.jpg', 'Icon 8'),
        ('static/user/icon9.jpg', 'Icon 9'),
    ], validators=[DataRequired()], default='static/user/default.jpg')
    
    password1 = PasswordField(label='New Password:', validators=[Optional(), Length(min=6)])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1', message='The passwords entered do not match. Please enter both passwords carefully.'), Optional()])
    submit = SubmitField(label='Save Changes')

class ReviewForm(FlaskForm):
    rating = IntegerField('Rating (1-5):', validators=[
        DataRequired(), NumberRange(min=1, max=5, message='Rating must be between 1 and 5')])
    review_text = TextAreaField('Review:', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Submit Review')