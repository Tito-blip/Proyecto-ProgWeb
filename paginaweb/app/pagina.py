from flask import Flask, render_template
from views import views_pagina # Importa el blueprint de las vistas
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:1234@192.168.61.172:5432/Empleados' # Conexion con Postgre

app.register_blueprint(views_pagina) # Registrar el blueprint de las vistas para que sean reconocidas por la app

# Iniciar la base de datos y crear las tablas definidas en el archivo models

db.init_app(app)

with app.app_context():
    db.create_all()