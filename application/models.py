from application import db

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_removed = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

        ## ALTER DATE REMOVED