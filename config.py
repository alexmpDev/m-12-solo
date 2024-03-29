from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, environ.get('SQLITE_FILE_RELATIVE_PATH'))
    IMAGES_UPLOAD_PATH = environ.get('IMAGES_UPLOAD_PATH')  
    BASEDIR = basedir  # Añade basedir como un atributo de la clase Config
    DEBUG = environ.get('DEBUG', False) == 'True'
    # Configuració per a Flask-DebugToolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    LOG_LEVEL = environ.get('LOG_LEVEL', 'DEBUG').upper()