import os
from dotenv import load_dotenv

load_dotenv()

# ✅ Get absolute path to app folder
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')

    # ✅ FIXED (absolute path)
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///lab5.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False