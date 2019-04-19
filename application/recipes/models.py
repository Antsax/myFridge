from application import db
from application.models import Base

class Recipe(Base):

    name = db.Column(db.String(144), nullable = False)
    instructions = db.Column(db.String, nullable = False)
    diet = db.Column(db.String(50), nullable = True)
    timeInMinutes = db.Column(db.Integer, nullable = True)

    def __init__(self, name, instructions, diet, timeInMinutes):
        self.name = name
        self.instructions = instructions
        self.diet = diet
        self.timeInMinutes = timeInMinutes