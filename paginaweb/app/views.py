import requests # Libreria peticiones HTTP
import json
from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from models import Empleados, Contact, User
from extensions import db
from forms import ContactoForm
from datetime import date

views_pagina = Blueprint('views_pagina', __name__) # Genera un blueprint para manejar las vista en el archivo principal

try:
    r = requests.get("https://jsonplaceholder.typicode.com/albums/1/photos") # Peticion GET a la API ** Se pude limitar con ?id=1**
    if r.status_code == 200: # Manejar errores del request # 
        resp = r.json() # Procesar la respuesta como JSON
        with open('response.json', 'w') as rp: # Escribir la respuesta de la API a archivo Json
            json.dump(resp, rp) # Formatear el JSON con dump. *Para escribir al archivo se necesita pasar un string*
except:
    pass

current_date = date.today()

# Rutas Principales #

@views_pagina.route("/")
def index():
    return render_template('pages/index.html')
                                                   
@views_pagina.route("/table")
@login_required
def table():
    base = db.session.query(Empleados).all() # Retrieve de la tabla Empleados
    return render_template('pages/table.html', base = base, name = current_user.name) # Mostrar los datos [Read / Retrieve]

@views_pagina.route("/contacto", methods=['GET', 'POST'])
def contacto():
    form = ContactoForm()

    if (request.method == 'POST') and form.validate():
        
        name = form.name.data
        lastname = form.lastname.data
        email = form.email.data
        gender = form.gender.data
        message = form.message.data
        
        mensaje = Contact(name, lastname, email, gender, message)

        db.session.add(mensaje)
        db.session.commit()

        flash('Mensaje Enviado!', category='success')

        return redirect(url_for('views_pagina.contacto'))

    return render_template('forms/contacto.html', form = form)

@views_pagina.route('/profile')
@login_required
def profile():
    return render_template('pages/perfil.html')

@views_pagina.route('/profileEmp')
@login_required
def profileEmp():
    if current_user.is_emp:
        return render_template('pages/perfilEmp.html')
    return abort(401)

@views_pagina.route("/tableUser")
@login_required
def table_user():
    base = db.session.query(User).all() # Retrieve de la tabla Empleados
    return render_template('pages/tableUser.html', base = base, current_date = current_date)

# Metodos para manejar formulario CRUD #

@views_pagina.route("/tableAdd", methods=['POST']) # Agregar registro
@login_required
def add_table():
    if (request.method == 'POST'):
        name = request.form['name']
        age = request.form['age']
        photo = request.form['photo']
        datos = Empleados(name = name, age = age, photo = photo)
        db.session.add(datos)
        db.session.commit()
        
        flash(f"Empleado {name} agregado correctamente", category='success')

        return redirect('/table')    
    else:
        return abort(404) # Abortar cuando el metodo sea GET # 

# Redireccionar a la pagina de update para acceder a través del modal

@views_pagina.route('/tableUpdate_redirect')
@login_required
def redirect_update():
    id = request.args.get("id")

    if id:
        return redirect(url_for('views_pagina.update', id=id))
    return render_template("forms/update.html/<int:id>", methods=['GET','POST'])

@views_pagina.route("/tableUpdate/<int:id>", methods=['GET', 'POST']) # Actualizar, con metodo GET para mostrar datos anteriores
@login_required

def update(id):
    empleado = Empleados.query.get(id)

    if not empleado:
        return abort(404)

    if request.method == "POST":        
            empleado.name = request.form['name']
            empleado.age = request.form['age']
            empleado.photo = request.form['photo']

            db.session.commit()
            flash(f"Empleado actualizado correctamente", category='success')
            return redirect('/table')             
    return render_template("forms/update.html", empleado = empleado, id = id)

@views_pagina.route("/tableDelete/<int:id>", methods=['POST']) # Eliminar
@login_required
def delete(id):
    
    empleado = Empleados.query.get(id)
    
    if empleado and request.method == 'POST':
        db.session.delete(empleado)
        db.session.commit()

        flash(f'Empleado {empleado} eliminado!', category='success')

        return redirect("/table")
    
    return abort(404)

# Errores #

@views_pagina.app_errorhandler(401)
def unauthorized(e):
    return render_template('errors/401.html'), 401

@views_pagina.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@views_pagina.app_errorhandler(405) # Para evitar crear una plantilla nueva, se reutiliza la de 404 #
def page_not_found(e):
    return render_template('errors/404.html'), 405

@views_pagina.app_errorhandler(500)
def error_server(e):
    return render_template('errors/500.html'), 500

# Error personalizado para empleado not found #