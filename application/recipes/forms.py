from flask_wtf import FlaskForm
from wtforms import validators, StringField, IntegerField, TextAreaField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2), validators.required()])
    instructions = TextAreaField("Instructions", [validators.required(), validators.Length(min=50)])
    diet = StringField("Diet(s)", [validators.optional()])
    timeInMinutes = IntegerField("Time in minutes", [validators.optional()])

    class Meta:
        csrf = False