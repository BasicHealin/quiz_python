import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
import flask
from flask import request, jsonify
import json 
import pandas as pd
from controllers.config import client

def convert_db(name_db,name_col, category):
    mydb = client[name_db]
    mycol = mydb[name_col]
    cursor = mycol.find({"category" : category},projection ={"_id" : 0})
    list_cur = list(cursor)
    df = pd.DataFrame(list_cur)
    return df

def read_post_db(name_db,name_col):
    mydb = client[name_db]
    mycol = mydb[name_col]
    cursor = mycol.find({},projection ={"_id" : 0})
    list_cur = list(cursor)
    df = pd.DataFrame(list_cur)
    return df

def concat_df(df1,df2):
    df=pd.merge(df1,df2, on='id', how='left')
    return df

