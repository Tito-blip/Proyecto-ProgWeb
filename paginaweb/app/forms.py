from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, URLField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Length, Regexp, InputRequired

# Clases de formularios WTForms para utilizar en las templates #

# Formularios Auth

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Regexp(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Email invalido"), Length(10, 100)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(8, 100)])
    remember = BooleanField('Recuerdame')
    submit = SubmitField('Ingresar')

class RegisterForm(FlaskForm):
    rut = StringField('Rut', validators=[InputRequired(), Regexp(regex=r'^\d{9}$', message="Compruebe el Rut ingresado")])    
    name = StringField('Nombre', validators=[InputRequired(), Length(4, 40)])
    email = EmailField('Email', validators=[InputRequired(), Regexp(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Email invalido"), Length(10, 100)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Regexp(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"), Length(8, 100)])
    phone = StringField('Telefono', validators=[InputRequired(), Regexp(regex=r'^\d{9}$', message="Compruebe el telefono ingresado")])     
    address = StringField('Dirección', validators=[InputRequired(), Length(20, 60)])
    photo = URLField('Foto Url')
    submit = SubmitField('Crear Cuenta')

# Formulario Contacto

class ContactoForm(FlaskForm):
    rut = StringField('Rut', validators=[InputRequired(), Regexp(regex=r'^\d{9}$', message="Compruebe el Rut ingresado")])
    name = StringField('Nombre', validators=[InputRequired(), Length(4, 40)])
    lastname = StringField('Apellido', validators=[InputRequired(), Length(4, 40)])
    email = EmailField('Email', validators=[InputRequired(), Regexp(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Email invalido"), Length(10, 100)])
    phone = StringField('Telefono', validators=[InputRequired(), Regexp(regex=r'^\d{9}$', message="Compruebe el telefono ingresado")])
    message = TextAreaField('Escribe tu mensaje...', validators=[InputRequired(), Length(20, 250)])
    submit = SubmitField('Enviar')

# Formulario Clientes

class ClienteForm(FlaskForm):
    rut = StringField('Rut', validators=[InputRequired(), Regexp(regex=r'^\d{9}$', message="Compruebe el Rut ingresado")])
    name = StringField('Nombre', validators=[InputRequired(), Length(4, 40)])
    email = EmailField('Email', validators=[InputRequired(), Regexp(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Email invalido"), Length(10, 100)])
    phone = StringField('Telefono', validators=[InputRequired(), Regexp(regex=r'^\d{9}$', message="Compruebe el telefono ingresado")])
    address = StringField('Dirección', validators=[InputRequired(), Length(20, 60)])
    company = StringField('Compañia', validators=[InputRequired(), Length(7, 40)])
    submit = SubmitField('Enviar')

# Formularios CRUD

# Agregar Form

# Update Form