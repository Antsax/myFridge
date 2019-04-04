from application import db
from application.models import Base

class Review(Base):

    title = db.Column(db.String(144), nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    comment = db.Column(db.String, nullable = True)

    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable = True)
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable = True)

    def __init__(self, title, rating, comment):
        self.title = title
        self.rating = rating
        self.comment = comment