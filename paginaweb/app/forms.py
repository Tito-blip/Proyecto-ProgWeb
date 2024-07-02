from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, URLField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField
from wtforms.validators import Length, DataRequired, Email, Regexp

# Clases de formularios WTForms para utilizar en las templates #

# Formularios Auth

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(10, 100)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(8, 100)])
    remember = BooleanField('Recuerdame')
    submit = SubmitField('Ingresar')

class RegisterForm(FlaskForm):
    rut = StringField('Rut', validators=[DataRequired(), Regexp(r'^\d{9}$')])    
    name = StringField('Nombre', validators=[DataRequired(), Length(4, 40)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(10, 100)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(8, 100)])
    phone = StringField('Telefono', validators=[DataRequired(), Regexp(r'^\d{9}$')])    
    address = StringField('Dirección', validators=[DataRequired(), Length(20, 60)])
    photo = URLField('Foto Url')
    submit = SubmitField('Crear Cuenta')

# Formulario Contacto

class ContactoForm(FlaskForm):
    rut = StringField('Rut', validators=[DataRequired(), Regexp(r'^\d{9}$')])    
    name = StringField('Nombre', validators=[DataRequired(), Length(4, 40)])
    lastname = StringField('Apellido', validators=[DataRequired(), Length(4, 40)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(10, 100)])
    phone = StringField('Telefono', validators=[DataRequired(), Regexp(r'^\d{9}$')])
    message = TextAreaField('Escribe tu mensaje...', validators=[DataRequired(), Length(20, 250)])
    submit = SubmitField('Enviar')

# Formulario Clientes

class ClienteForm(FlaskForm):
    rut = StringField('Rut', validators=[DataRequired(), Regexp(r'^\d{9}$')])
    name = StringField('Nombre', validators=[DataRequired(), Length(4, 40)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(10, 100)])
    phone = StringField('Telefono', validators=[DataRequired(), Regexp(r'^\d{9}$')])
    address = StringField('Dirección', validators=[DataRequired(), Length(20, 60)])
    company = StringField('Compañia', validators=[DataRequired(), Length(7, 40)])
    submit = SubmitField('Enviar')

# Formularios CRUD

# Agregar Form

# Update Form