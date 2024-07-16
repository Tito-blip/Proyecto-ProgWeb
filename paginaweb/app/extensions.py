# Inicializar en este archivo para evitar circularidad, luego inicializar en archivo de la app #

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.loging_view = 'auth.login'