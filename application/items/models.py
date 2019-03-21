from application import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, default=db.func.current_timestamp())

    # ALTER DATE_REMOVED LATER
    date_removed = db.Column(db.DateTime, default = db.func.current_timestamp(),  
    onupdate = db.func.current_timestamp())                                       
    # EXPIRATION DATE HERE

    name = db.Column(db.String(144), nullable=False)
    vegan = db.Column(db.Boolean, nullable = False)

    # PRODUCT_TYPE HERE

    def __init__(self, name):
        self.name = name
        self.vegan = False
    