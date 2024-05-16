# import Flask from flask module
from flask import Flask

# create a server
server = Flask(__name__)

@server.route('/')
def homepage():
    return "This is Home Page"

@server.route('/welcome')
def welcome():
    return "Welcome to IoT Application"


# run server
server.run(host='0.0.0.0')

# Running on http://127.0.0.1:5000
# Running on http://172.18.7.60:5000