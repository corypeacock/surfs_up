#! python

# dependencies
from flask import Flask 

# create new flask app instance
app = Flask(__name__)

# create Flask routes
# starting point is the root
@app.route('/')

# function
def hello_world():
    return 'Hello world'
    
