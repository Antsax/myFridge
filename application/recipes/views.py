from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required, logout_user

from application import app, db
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

@app.route("/recipes/", methods = ["GET"])
def recipes_index():
    return render_template("recipes/index.html", recipes = Recipe.query.all())

@app.route("/recipes/<recipe_id>/<recipe_name>", methods = ["GET"])
@login_required
def recipe_view(recipe_id, recipe_name):
    return render_template("recipes/recipe.html", recipes = Recipe.query.filter_by(id = recipe_id), recipe_name = recipe_name)

@app.route("/recipes/new", methods = ["GET", "POST"])
@login_required
def recipe_form():
    if request.method == "GET":
        return render_template("/recipes/create.html", form = RecipeForm())

    form = RecipeForm(request.form)

    if not form.validate:
        return render_template("/recipes/create.html", form = form)

    r = Recipe(form.name.data, form.instructions.data, form.diet.data, form.timeInMinutes.data)
    db.session().add(r)
    db.session().commit()

    return redirect(url_for("recipes_index"))