"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
# DO NOT TOUCH!!!
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
# END DO NOT TOUCH!!!

#Our code :-)

# Import all of our routes from routes.py
from routes import *;

# Launching our server
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
