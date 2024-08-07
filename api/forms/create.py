# from wtforms.csrf.session import SessionCSRF
# from datetime import timedelta
from wtforms import StringField, validators, SubmitField
from flask_wtf import FlaskForm

# class MyBaseForm(FlaskForm):
#     class Meta:
#         csrf = True
#         csrf_class = SessionCSRF
#         csrf_secret = b"EPj00jpfj8Gx1SjnyLxwBBSQfnQ9DJYe0Ym"
#         csrf_time_limit = timedelta(minutes=20)


class PostCreateForm(FlaskForm):
    title = StringField('Title',[validators.InputRequired(
        message="Title should not be empty."
    )])
    description = StringField('Description')
    submit = SubmitField('Submit') 
