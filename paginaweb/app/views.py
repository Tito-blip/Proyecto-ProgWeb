import requests # Libreria peticiones HTTP
import json
from flask import Blueprint, render_template, request, redirect
from models import db, Api, Empleados

views_pagina = Blueprint('views_pagina', __name__) # Genera un blueprint para manejar las vista en el archivo principal

r = requests.get("https://jsonplaceholder.typicode.com/albums/1/photos") # Peticion GET a la API
resp = r.json() # Procesar la respuesta como JSON
with open('response.json', 'w') as rp: # Escribir la respuesta de la API a archivo Json
    json.dump(resp, rp) # Formatear el JSON con dump. *Para escribir al archivo se necesita pasar un string*

# Rutas Principales #

@views_pagina.route("/")
def index():
    return render_template('pages/index.html')
                                                   
@views_pagina.route("/table")
def table():
    base = db.session.query(Empleados).all() # Retrieve de la DB
    return render_template('pages/table.html', base= base) # Mostrar los datos [Read / Retrieve]

@views_pagina.route("/api")
def api():
    json_api = Api(json_column=resp)
    db.session.add(json_api)
    db.session.commit() # Escribir respuesta de la API a DB
    return render_template('api/tabla-api.html', resp = resp)

# Metodos para manejar formulario CRUD #

@views_pagina.post("/tableAdd") # Agregar registro
def add_table():
    if (request.method == 'GET'):
        return redirect('/table')    
    else:
        name = request.form['name']
        age = request.form['age']
        photo = request.form['photo']
        datos = Empleados(name = name, age = age, photo = photo)
        db.session.add(datos)
        db.session.commit()
        print(photo)
        return redirect('/table')

@views_pagina.route("/tableUpdate/<id>", methods=['POST', 'GET']) # Actualizar, con metodo GET para mostrar datos anteriores
# o.O #
def update(id):
    empleado = Empleados.query.get(id)
        
    if request.method == "POST":        
            empleado.name = request.form['name']
            empleado.age = request.form['age']
            empleado.photo = request.form['photo']

            db.session.commit()
            return redirect('/table')     
    return render_template("pages/update.html", empleado = empleado, id = id)

@views_pagina.route("/tableDelete/<id>") # Eliminar
def delete(id):
    empleado = Empleados.query.get(id)
    db.session.delete(empleado)
    db.session.commit()

    return redirect("/table")

# Errores #

@views_pagina.app_errorhandler(404)
def page_not_found(error):
    render_template('layouts/404.html'), 404

@views_pagina.app_errorhandler(500)
def error_server(error):
    return render_template('layouts/500.html'), 500