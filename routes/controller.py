from controllers.getdb import *
from controllers.postoptions import *
from flask import Blueprint
from flask import request

table = Blueprint('table', __name__)




@table.route('/getdb', methods=['GET'])
def get_db():
    category = request.args.get('category')
    return getDB_(category)

@table.route('/postoptions', methods=['POST'])
def getpost_score():
    return postoptions()

