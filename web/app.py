import os
from flask import Flask
from config import PostgreSQL


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test:test@db:5432/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False