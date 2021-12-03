from flask import (abort, 
                jsonify, 
                make_response)
from datetime import datetime
from .app import app
from db.models import db, User
from config import error_number, Routes


@app.route(Routes.route_def, methods=['GET'])
def make_basic_values() -> None:
    return 'Hello World'

@app.route(Routes.route_id, methods=['GET'])
def get_user_id(id) -> str:
    """
    Function which is dedicated to develop the 
    Input:  id = id which is going to be searched
    Output: datetime value of its creation
    """
    if not id.isdigit():
        return abort(error_number)
    value_return = User.query.filter_by(id=id).first()
    if value_return:
        return f'Your datetime: {value_return.date};'
    return abort(error_number)
    
@app.route(Routes.route_user_ins, methods=['GET', 'POST'])
def make_basic_insert() -> str:
    """
    Function for basic insertion to the values
    Input:  None
    Output: we created new values
    """
    value_date = datetime.now()
    db.session.add(User(date=value_date))
    db.session.commit()
    return f'We inserted user at time: {value_date}'

@app.route(Routes.route_user_ret, methods=['GET', 'POST'])
def check_user() -> dict:
    """
    Function which is dedicated to show all users 
    which are presented within the database
    Input:  None
    Output: json value of the created value
    """
    return make_response(
        jsonify(
            {k.id: k.date 
            for k in User.query.all()
            }), 
        200)