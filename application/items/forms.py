from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ItemForm(FlaskForm):
    name = StringField("Item name", [validators.Length(min=2)])
    vegan = BooleanField("Vegan")

    class Meta:
        csrf = False