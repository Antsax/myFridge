from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required, logout_user

from application import app, db, login_required, login_manager
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

@app.route("/recipes/", methods = ["GET"])
def recipes_index():
    return render_template("recipes/index.html", recipes = Recipe.query.all())