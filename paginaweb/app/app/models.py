from sqlalchemy import Date
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func
from extensions import db
from flask_login import UserMixin

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

# Modelo de usuarios #

class User(UserMixin, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True ,nullable=False)
    password = db.Column(db.String(150), nullable=False)
    photo = db.Column(db.String(255), nullable=True)
    date = db.Column(Date(), default=func.now(), onupdate=func.now())
    role = db.Column(db.String(50), nullable=False, default="User")
    is_emp = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, name, email, password, photo, is_emp):
        self.name = name
        self.email = email
        self.password = password
        self.photo = photo
        self.is_emp = is_emp

    def __repr__(self):
        return self.name

class Contact(UserMixin, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    lastname = db.Column(db.String(40))
    email = db.Column(db.String(65), unique=True ,nullable=False)
    gender = db.Column(db.String(15), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), default='En Proceso')

    def __init__(self, name, lastname, email, gender, message):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.gender = gender
        self.message = message


    def __repr__(self):
        return self.name

class Api(db.Model): # Tabla para guardar la respuesta API en Json
    id = db.Column(db.Integer, primary_key=True)
    json_column = db.Column(JSON)