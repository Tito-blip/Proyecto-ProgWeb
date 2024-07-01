from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, URLField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import Length, DataRequired, Email
from email_validator import validate_email

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(10, 100)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(8, 100)])
    remember = BooleanField('Recuerdame')
    submit = SubmitField('Ingresar')

class RegisterForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(4, 40)])
    email = EmailField('Email', validators=[DataRequired(), Email(check_deliverability=True), Length(10, 100)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(8, 100)])
    photo = URLField('Foto Url')
    submit = SubmitField('Crear Cuenta')

# Formulario Contacto

class ContactoForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(4, 40)])
    lastname = StringField('Apellido', validators=[DataRequired(), Length(4, 40)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(10, 100)])
    gender = SelectField('Cual es tu genero?', choices=[('Masculino'), ('Femenino'), ('Otro')])
    message = TextAreaField('Escribe tu mensaje...', validators=[Length(20, 250)])
    submit = SubmitField('Enviar')

# Formularios CRUD

# Agregar Form

# Update Form