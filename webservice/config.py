import os
from dotenv import load_dotenv

load_dotenv()

error_number = 404

class FlaskServer:
    host = '0.0.0.0'

class PostgreSQL:
    db = os.getenv('POSTGRES_DB')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    default = ''.join(['sqlite:///', os.path.join(os.getcwd(), 'db.sqlite')])

class Routes:
    route_def = '/'
    route_user_ins = '/user_insert'
    route_user_ret = '/user_return'
    route_id = '/id/<id>'