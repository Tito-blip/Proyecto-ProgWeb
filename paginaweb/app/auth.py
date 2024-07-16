from flask import Blueprint, redirect, url_for, request, render_template, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from forms import LoginForm, RegisterForm
from models import User, Contact, Clientes
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db, login_manager

auth = Blueprint('auth', __name__) # Blueprint de auth para conectar con la app

@login_manager.user_loader # Definir loader de usuarios para Flask-Login
def load_user(id):
    user = User.query.get(int(id))
    if user:
        return user
    return None

# Vistas de Flask-Admin #

class ClientView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

    can_create = True
    can_edit = False

class UserView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

    column_list = ('id', 'name', 'email') # Definir columnas de la tabla y si se pueden ordenar o buscar
    column_sortable_list = ('id', 'name') 
    column_searchable_list = ('name', 'email')
    form_excluded_columns = ('password', 'photo', 'is_admin') # No incluir columnas en el formulario de admin

class ContactView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin # Restringir a usuario admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login')) # Redirige a login cuando falla la autorizacion de admin

    def _description_formatter(view, context, model, name):
        return model.message[:20] # Reducir el mensaje mostrado en las columnas a 20 caracteres

    column_list = ('id', 'name', 'lastname', 'email', 'gender', 'message', 'status') # Definir columnas que se mostraran en la tabla
    column_sortable_list = ('id', 'name', 'lastname', 'email', 'status') 
    column_searchable_list = ('name', 'lastname', 'email', 'status')
    can_create = False # Deshabilitar la creacion de nuevas entradas
    form_choices = { # Seleccion para diferentes status
    'status': [
        ('Ingresado', 'Ingresado'),
        ('Sugerencia' ,'Sugerencia'),        
        ('Reclamo' ,'Reclamo'),
        ('Soporte', 'Soporte'),
        ('Respondido', 'Respondido'),
        ('Eliminar', 'Eliminar')
        ]
    }
    
    form_widget_args = { # Definir campos como readonly para que no sean modificados
        'rut': {
            'readonly': True
        },
        'name': {
            'readonly': True
        },
        'lastname': {
            'readonly': True
        },
        'phone': {
            'readonly': True
        },
        'date': {
            'readonly': True
        },
        'email': {
            'readonly': True
        },
        'message': {
            'readonly': True
        },
    }
    
class MyAdminIndexView(AdminIndexView): # Vista principal para dashboard admin #
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

    @expose('/')
    def index(self):
        if not current_user.is_authenticated and current_user.is_admin:
            return redirect(url_for('auth.login'))
        return super(MyAdminIndexView, self).index()

# Tablas Admin Dashboard

admin = Admin(name='Tabla Admin', template_mode='bootstrap4', index_view=MyAdminIndexView(name='Home')) # Crear vista principal de admin
admin.add_view(UserView(User, db.session)) # Agregar vistas basadas en los modelos creados en models.py
admin.add_view(ContactView(Contact, db.session, name="Formularios Contacto"))
admin.add_view(ClientView(Clientes, db.session, name="Clientes"))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() # Utilizar formulario de la clase en forms.py (WTForms)

    if (request.method == 'POST') and form.validate():

        email = form.email.data
        password = form.password.data
        remember = form.remember.data

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('No existe un usuario con esas credenciales. <a href="' + url_for('auth.register') + '"> <b>Crear una cuenta.</b> </a>', 'danger')
            return redirect(url_for('auth.login'))
        
        if user and not check_password_hash(user.password, password): # Comprueba el hash de la contraseña con el input del form
            flash('Compruebe las credenciales.', category="warning")
            return redirect(url_for('auth.login'))

        login_user(user, remember = remember)
        flash('Sesión iniciada correctamente', category='success') # Devuelve un mensaje flash para mostrar al usuario
        return redirect(url_for('views_pagina.index'))

    return render_template('auth/login.html', form = form)

@auth.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if (request.method == 'POST') and form.validate():

        rut = form.rut.data
        name = form.name.data
        email = form.email.data 
        phone = form.phone.data
        address = form.address.data 
        password = form.password.data
        photo = form.photo.data

        # Comprobar el email, si ya existe envia mensaje flash #

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Ese usuario ya esta registrado!', category="danger")
            return redirect(url_for('auth.register'))

        # Si no existe el usuario, lo registra en la DB y redirige a la pagina de login #

        new_user = User(rut = rut, name=name, email=email, phone=phone, address=address, password=generate_password_hash(password, method='pbkdf2'), photo = photo)

        db.session.add(new_user)
        db.session.commit()

        flash('Usuario registrado correctamente!', category="success")

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Se ha cerrado la sesión." , category='success')
    return redirect(url_for('views_pagina.index'))