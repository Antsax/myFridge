from application import app, db
from flask import render_template, request, url_for, redirect
from application.items.models import Item

@app.route("/items/new/")
def items_form():
    return render_template("items/new.html")

@app.route("/items/", methods=["POST"])
def items_create():
    i = Item(request.form.get("name"))
    
    db.session().add(i)
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/<item_id>/", methods = ["POST"])
def items_set_vegan(item_id): # VALITSE JOKU MUU KUIN DONE, MUOKKAA MODELS.PY
    i = Item.query.get(item_id)
    i.vegan = True
    db.session().commit()
    return redirect(url_for("items_index"))
    