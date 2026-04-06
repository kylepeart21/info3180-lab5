from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()  # ✅ create without app first

app = Flask(__name__)
app.config.from_object(Config)

# ✅ now attach everything to app
db.init_app(app)
migrate.init_app(app, db)
csrf.init_app(app)

from app import views
from app import models