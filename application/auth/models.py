from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable = False)
    username = db.Column(db.String(144), nullable = False)
    password = db.Column(db.String(144), nullable = False)

    items = db.relationship("Item", backref='account', lazy = True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]

    @staticmethod
    def find_users_with_no_items(vegan = True):
        stmt = text("SELECT Account.id, Account.name FROM ACCOUNT"
                    " LEFT JOIN Item ON Item.account_id = Account.id"
                    " WHERE (Item.vegan IS null OR Item.vegan = :vegan)"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Item.id) = 0").params(vegan=vegan)
                
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response