
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

@app.route("/")

def home():
    return "Hello, Flask page"
