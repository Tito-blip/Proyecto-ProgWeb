from flask import Flask
from views import views_pagina  # Importa el blueprint de las vistas
from auth import auth, admin
from extensions import db, login_manager

app = Flask(__name__)

# Se establece la clave por convencion, ya que no es relevante para este caso #
# En otras circunstancias se debe mantener en secreto #
app.secret_key = '97c27c7351b75853c654ce714a18b47f4a6399263b33a7d920ca2eb8d2d8c354'

#Cambiar DATABASE_URI por PostgreSQL o Sqlite para utilizar una de las dos BD
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://user:password@localhost:5432' # Conexión con PostgreSQL
#app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///local_db.sqlite' # Conexión con sqlite en reemplazo de postgres

app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'lux'
app.config['FLASK_ADMIN_SWATCH'] = 'lux'

app.register_blueprint(views_pagina) # Registrar el blueprint de las vistas para que sean reconocidas por la app
app.register_blueprint(auth)

# Definir el manejo de login, para el uso de sesiones

login_manager.init_app(app)

# Iniciar admin #

admin.init_app(app)

# Iniciar la base de datos y crear las tablas definidas en el archivo models

db.init_app(app)

with app.app_context():
    db.create_all()