from routes.controller import *
from flask import Flask
from flask_cors import CORS
from bson.json_util import dumps


app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = True

@app.errorhandler(404)
def handle_404(err):
    return dumps({'success': False, 'error': 404})


@app.errorhandler(500)
def handle_500(err):
    return dumps({'success': False, 'error': 500})


@app.errorhandler(401)
def handle_401(err):
    return dumps({'success': False, 'error': 401})
