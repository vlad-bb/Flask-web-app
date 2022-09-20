import pathlib
from dotenv import dotenv_values

BASE_DIR = pathlib.Path(__file__).parent.parent
config = dotenv_values(".env")


class Config:
    UPLOAD_FOLDER = str(BASE_DIR / 'uploads')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'data' / 'app.db.sqlite3')
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:8GAnRayUnSR5EpC7@provisioning:5432/postgres'
    # SECRET_KEY = config['SECRET_KEY']
    SECRET_KEY = 'super_secret_app_007'
