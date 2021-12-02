import os
from dotenv import load_dotenv

load_dotenv()

error_number = 404

host = '0.0.0.0'

class PostgreSQL:
    default = ''.join(['sqlite:///', os.path.join(os.getcwd(), 'db.sqlite')])

class Routes:
    route_def = '/'
    route_user_ins = '/user_insert'
    route_user_ret = '/user_return'
    route_id = '/id/<id>'