from web.app import app
from web.routes import *
from config import host


if __name__ == '__main__':
    app.run(host=host)