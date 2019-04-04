from application import db
from application.models import Base

class Item(Base):
    # EXPIRATION DATE HERE

    name = db.Column(db.String(144), nullable=False)
    vegan = db.Column(db.Boolean, nullable = False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)

    # PRODUCT_TYPE HERE

    def __init__(self, name):
        self.name = name
        self.vegan = False
    