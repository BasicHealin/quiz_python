import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
from flask import request, jsonify
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
import flask
from flask import request, jsonify
import json 
import pandas as pd
from controllers.readdb import *
from controllers.randomquestions import *


def getDB_(category):
    
    name_db="Quiz"
    name_col="option"
    df1=convert_db(name_db,name_col,category)
    
    result = df1.to_json(orient="records")
    parsed = json.loads(result)
    json_nedeed=json.dumps(parsed, indent=4)  
    return json_nedeed
