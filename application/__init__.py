# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy

import os

# Kun ollaan Herokussa, käytetään Herokun tietokantaa, muulloin omaa
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    # Käytetään items.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
    # kertoo, että tiedosto sijaitsee tämän sovelluksen tiedostojen 
    # kanssa samassa paikassa
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"
    # Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)



# Lisätään kirjautumisen toiminallisuus
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please log in to use this functionality."



# Määritellään rooleja tukeva dekoraattori
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
          
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
    


# Luetaan kansiosta application tiedoston views sisältö
from application import views

# Luetaan kansiosta items tiedoston models ja views sisältö
from application.items import models
from application.items import views

# Luetaan kansiosta auth tiedoston models ja views sisältö
from application.auth import models
from application.auth import views

# Luetaan kansiosta reviews tiedoston models ja views sisältö
from application.reviews import models
from application.reviews import views


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut
try:
    db.create_all()
except:
    pass