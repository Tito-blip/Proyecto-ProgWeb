import requests # Libreria peticiones HTTP
import json
from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from models import Clientes, Contact, User, Api
from extensions import db
from forms import ContactoForm, ClienteForm
from datetime import date

views_pagina = Blueprint('views_pagina', __name__) # Genera un blueprint para manejar las vista en el archivo principal

try:
    r = requests.get("https://jsonplaceholder.typicode.com/albums/1/photos?id=1") # Peticion GET a la API ** Se pude limitar con ?id=1**
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

@views_pagina.route("/destinos")
def destinos():
    return render_template('pages/destinos.html')         

@views_pagina.route("/nosotros")
def nosotros():
    return render_template('pages/sobre_nosotros.html')                                 

@views_pagina.route("/table")
@login_required # Decorador para permitir acceso solo a usuarios logeados #
def table():
    form = ClienteForm()

    if current_user.is_emp or current_user.is_admin:
        base = db.session.query(Clientes).all() # Retrieve de la tabla
        return render_template('pages/table.html', base = base, current_date = current_date, form = form) # Mostrar los datos
    return abort(401)

@views_pagina.route("/tableApi")
@login_required
def tableApi():
    # Por simplicidad se comprueba directamente el permiso, se podria utilizar una libreria (Flask-Principal) junto con flask-login para mas seguridad #
    if current_user.is_emp or current_user.is_admin: # Comprueba si el usuario es empleado o admin
        try:
            json_api = Api(json_column=resp)
            db.session.add(json_api)
            db.session.commit() # Escribir respuesta de la API a DB
        except:
            return flash('Error al conectar a la API!', category='danger') # Si falla muestra error 500 y mensaje flash
        
        return render_template('api/tabla-api.html', resp = resp)
    abort(401)

@views_pagina.route("/contacto", methods=['GET', 'POST'])
def contacto():
    form = ContactoForm()

    if (request.method == 'POST') and form.validate():
        
        rut = form.rut.data
        name = form.name.data
        lastname = form.lastname.data
        email = form.email.data
        phone = form.phone.data
        message = form.message.data
        
        mensaje = Contact(rut, name, lastname, email, phone, message)

        db.session.add(mensaje)
        db.session.commit()

        flash('Mensaje Enviado!', category='success')

        return redirect(url_for('views_pagina.contacto'))

    return render_template('forms/contacto.html', form = form)

@views_pagina.route("/mensajes")
def mensajes():
    if current_user.is_emp or current_user.is_admin:
        base = db.session.query(Contact).all()
        return render_template('pages/tableMensajes.html', base = base)
    return abort(401)

@views_pagina.route('/profile')
@login_required
def profile():
    return render_template('pages/perfil.html')

@views_pagina.route('/profileEmp')
@login_required
def profileEmp():
    if current_user.is_emp or current_user.is_admin:
        return render_template('pages/perfilEmp.html')
    return abort(401)

@views_pagina.route("/tableUser")
@login_required
def table_user():
    if current_user.is_emp or current_user.is_admin:
        base = db.session.query(User).all() # Retrieve de la tabla User
        return render_template('pages/tableUser.html', base = base, current_date = current_date)
    return abort(401)

# Metodos para manejar formulario CRUD #

@views_pagina.route("/tableAdd", methods=['POST']) # Agregar registro
@login_required
def add_table():

    form = ClienteForm()

    if (request.method == 'POST') and form.validate() and (current_user.is_emp or current_user.is_admin):
        
        rut = form.rut.data
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        address = form.address.data
        company = form.company.data

        cliente = Clientes(rut, name, email, phone, address, company)

        db.session.add(cliente)
        db.session.commit()

        flash('Cliente Creado!', category='success')

        return redirect(url_for('views_pagina.table'))   

    else:
        return abort(404) # Abortar cuando el metodo sea GET # 

# Redireccionar a la pagina de update para acceder a través del modal

@views_pagina.route('/tableUpdate_redirect')
@login_required
def redirect_update():
    id = request.args.get("id")

    if id and (current_user.is_emp or current_user.is_admin):
        return redirect(url_for('views_pagina.update', id=id))
    return render_template("forms/update.html/<int:id>", methods=['GET','POST'])

@views_pagina.route("/tableUpdate/<int:id>", methods=['GET', 'POST']) # Actualizar, con metodo GET para mostrar datos anteriores
@login_required

def update(id):
    cliente = Clientes.query.get(id)

    if not cliente:
        return abort(404)

    if request.method == "POST" and cliente and (current_user.is_emp or current_user.is_admin):        
            cliente.rut = request.form['rut']
            cliente.name = request.form['name']
            cliente.email = request.form['email']
            cliente.phone = request.form['phone']
            cliente.address = request.form['address']
            cliente.company = request.form['company']

            db.session.commit()
            flash(f"Cliente actualizado correctamente", category='success')
            return redirect('/table')             
    return render_template("forms/update.html", cliente = cliente, id = id)

@views_pagina.route("/tableDelete/<int:id>", methods=['POST']) # Eliminar
@login_required
def delete(id):
    
    cliente = Clientes.query.get(id)
    
    if cliente and request.method == 'POST' and (current_user.is_emp or current_user.is_admin):
        db.session.delete(cliente)
        db.session.commit()

        flash(f'Cliente {cliente} eliminado!', category='success')

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