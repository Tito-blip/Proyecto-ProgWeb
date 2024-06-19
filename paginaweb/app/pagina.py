from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('pages/index.html')

@app.errorhandler(404) # Error page not found 404
def page_not_found(e):
    return render_template('layouts/404.html')