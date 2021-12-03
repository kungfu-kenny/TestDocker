import os
from flask import Flask
from config import PostgreSQL


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"postgresql://{PostgreSQL.user}:{PostgreSQL.password}@{PostgreSQL.host}:{PostgreSQL.port}/{PostgreSQL.db}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False