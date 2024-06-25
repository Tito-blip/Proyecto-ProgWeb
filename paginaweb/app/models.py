from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy() # Instanciar DB

# Crear un Modelo / Tabla para la base de datos

class Empleados(db.Model): # Tabla de ejemplo, con empleados
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(255), nullable=True)

    def __init__(self, name, age, photo):
        self.name = name,
        self.age = age,
        self.photo = photo

class Api(db.Model): # Tabla para guardar la respuesta API en Json
    id = db.Column(db.Integer, primary_key=True)
    json_column = db.Column(JSON)