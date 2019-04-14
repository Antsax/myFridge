from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application import app, db
from application.reviews.models import Review
from application.reviews.forms import ReviewFormItem

@app.route("/review/new/<item_id>", methods = ["GET", "POST"])
@login_required
def review_item(item_id):
    if request.method == "GET":
        return render_template("/reviews/reviewform.html", form = ReviewFormItem(), item_id = item_id)

    form = ReviewFormItem(request.form)

    if not form.validate:
        return render_template("/reviews/reviewform.html", form = form)

    r = Review(form.title.data, form.quality.data, form.comment.data)
    r.item_id = item_id
    db.session().add(r)
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/review/<item_id>/<item_name>", methods = ["GET"])
@login_required
def review_view(item_id, item_name):
    return render_template("reviews/review.html", reviews = Review.query.filter_by(item_id = item_id), item_name = item_name)