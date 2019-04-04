from flask_wtf import FlaskForm
from wtforms import validators, StringField, SelectField


class ReviewFormItem(FlaskForm):
    title = StringField("Title", [validators.length(min=5)])
    quality = SelectField("Quality", [validators.required()], choices=[('1', "poor"), ("2", "decent"), ("3", "good"), ("4", "very good"), ("5", "excellent")])
    comment = StringField("Comment", [validators.optional(), validators.length(min=10), validators.length(max=200)])

    class Meta:
        csrf = False