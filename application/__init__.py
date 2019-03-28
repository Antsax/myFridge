# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy

# Käytetään items.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, että tiedosto sijaitsee tämän sovelluksen tiedostojen 
# kanssa samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"

# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sisältö
from application import views

# Luetaan kansiosta items tiedoston models ja views sisältö
from application.items import models
from application.items import views

## Luetaan kansiosta auth tiedoston models sisältö
from application.auth import models

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()