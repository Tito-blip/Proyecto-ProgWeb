from sqlalchemy import Date
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func
from extensions import db
from flask_login import UserMixin

# Crear un Modelo / Tabla para la base de datos

class Clientes(UserMixin, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer(), unique=True, nullable=False)    
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True ,nullable=False)
    phone = db.Column(db.Integer(), unique=True, nullable=False)
    address = db.Column(db.String(60), unique=True, nullable=False)
    company = db.Column(db.String(60), unique=True, nullable=True)
    
    def __init__(self, rut, name, email, phone, address, company):
        self.rut = rut
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.company = company

# Modelo de usuarios #

class User(UserMixin, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer(), unique=True, nullable=False)
    name = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True ,nullable=False)
    phone = db.Column(db.Integer(), unique=True, nullable=False)
    address = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    photo = db.Column(db.String(255), nullable=True)
    date = db.Column(Date, default=func.now(), onupdate=func.now())    
    role = db.Column(db.String(50), nullable=False, default="User")
    is_emp = db.Column(db.Boolean, default=False) # Define flags de empleado y admin para comprobar con current_user
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, rut, name, email, phone, address, password, photo): # Inicializar modelo
        self.rut = rut
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.password = password
        self.photo = photo

    def __repr__(self):
        return self.name

class Contact(UserMixin, db.Model): # Los campos no son unicos, ya que la persona puede enviar varios mensajes
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer(), unique=True, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(65), nullable=False)
    phone = db.Column(db.Integer(), nullable=False)
    date = db.Column(Date, default=func.now(), onupdate=func.now())    
    message = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), default='Ingresado')

    def __init__(self, rut, name, lastname, email, phone, message):
        self.rut = rut
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.message = message

    def __repr__(self):
        return self.name

class Api(db.Model): # Tabla para guardar la respuesta API en Json
    id = db.Column(db.Integer, primary_key=True)
    json_column = db.Column(JSON)