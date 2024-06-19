<!-- https://github.com/othneildrew/Best-README-Template -->

<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/Tito-blip/Proyecto-ProgWeb">
    <img src="Paginaweb/static/img/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Aplicacion Flask y Servidor Web</h3>

  <p align="center">
    Repositorio Prueba Unidad 3
    <br />
    <br />
    <a href="https://github.com/Tito-blip/Proyecto-ProgWeb">Inicio</a>
    ·
    <a href="https://github.com/Tito-blip/Proyecto-ProgWeb/branches">Pruebas Anteriores</a>
    ·
    <a href="https://github.com/Tito-blip/Proyecto-ProgWeb/wiki">Wiki</a>
  </p>
</div>

<br>
<p style="text-align: justify"> 
El lenguaje HTML se utiliza para generar las plantillas que usará Flask. Por otro lado, se agregan funcionalidades utilizando JavaScript y Bootstrap. Por último, se utiliza la base de datos MongoDB para guardar los retornos de la API y las vistas.

Para el servidor, se utiliza una VM con Ubuntu Server, la cual posee un entorno virtual de Python donde se maneja la aplicación de Flask. Utilizando Gunicorn, se maneja todo lo relacionado con Flask. Finalmente, se utiliza Nginx para manejar y redirigir las conexiones entrantes, pasando por una redirección HTTPS y, adicionalmente, mostrar los archivos estáticos a través de Gunicorn.
 </p>

### Tecnologías
* ![HTML5]
* ![CSS]
* ![JS]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![Flask]][Flask-url] &nbsp; [![Jinja]][Jinja-url]
* [![MongoDB]][Mongo-url]

### Servidor
* ![Linux]
* [![Gunicorn]][Gunicorn-url]
* [![Nginx]][Nginx-url]

<!-- FOLDER STRUCTURE -->

### Estructura Proyecto

El proyecto se estructura en base al modelo MVT (Modelo - Vista - Plantilla). Utiliza modelos para estructurar la base de datos, vistas para manejar datos y crear las rutas de la app, y plantillas para estructurar las paginas.

<!-- Estructura base -->

```bash
├── envpaginaweb # Entorno virtual de python

├── paginaweb/
│    └── app/ # Carpeta root app
│	 ├── models # Modelos de la BD
│	 ├── templates # Plantillas Jinja [Carpeta por defecto en Flask]
│	   ├── pages
│	     ├── *.html
│          ├── layout # Plantillas "Esqueleto"
│            ├── base.html
│            ├── 404.html  
│	 ├── views # Vistas
├── static/ # Archivos estaticos
│    ├── css
│      ├── *.css
│    ├── img
│      ├── *.png	
│    ├── js
│      ├── *.js
└─ wsgi.py # Gunicorn
```
<br>

```python
# Archivo WSGI para iniciar con Gunicorn

from paginaweb import app

if  __name__  ==  "__main__":
app.run()
```

<!-- MARKDOWN BADGES -->

[HTML5]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[CSS]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[JS]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Jinja]: https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black
[Jinja-url]: https://jinja.palletsprojects.com/en/3.1.x/
[Nginx]: https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white
[Nginx-url]: https://nginx.org/en/
[Gunicorn]: https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white
[Gunicorn-url]: https://gunicorn.org/
[Linux]: https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black
[MongoDB]: https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white
[Mongo-url]: https://www.mongodb.com/
