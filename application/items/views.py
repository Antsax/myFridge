from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application import app, db
from application.items.models import Item
from application.items.forms import ItemForm

@app.route("/items/new/")
@login_required
def items_form():
    return render_template("items/new.html", form = ItemForm())

@app.route("/items/", methods=["POST"])
@login_required
def items_create():
    form = ItemForm(request.form)

    if not form.validate():
        return render_template("items/new.html", form = form)
    
    i = Item(form.name.data)
    i.vegan = form.vegan.data
    i.account_id = current_user.id

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/<item_id>/", methods = ["POST"])
@login_required
def items_set_vegan(item_id): # VALITSE JOKU MUU KUIN DONE, MUOKKAA MODELS.PY
    i = Item.query.get(item_id)
    i.vegan = True
    db.session().commit()
    return redirect(url_for("items_index"))

@app.route("/items/<item_id>/delete", methods = ["POST"])
@login_required
def item_delete(item_id):
    i = Item.query.get(item_id)
    db.session.delete(i)
    db.session.commit()
    return redirect(url_for("items_index"))
    