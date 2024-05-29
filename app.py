import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, g, abort, flash

app = Flask(__name__)

# Rota para index
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('site/about.html')

@app.route("/contact")
def contact():
    return render_template('site/contact.html')

@app.route("/projetos")
def projetos():
    return render_template('site/projetos.html')

if __name__ == "__main__":
    app.run(debug=True)