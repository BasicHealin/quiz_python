import json
import pandas as pd
import numpy as np
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
from controllers.readdb import *
from pandas.io.json import json_normalize
from controllers.config import client


def postoptions():
    #connet to mongo db
    mydb = client["Quiz"]
    mycol = mydb["User"]
    post=request.get_json()
    dfK = json_normalize(post)
    name_db="Quiz"
    name_col="correctanswers"
    dfN=dfK["name"][0]
    dfE=dfK["email"][0]
    dfP=dfK["phone"][0]
    dfEN=dfK["entreprise"][0]
    #calculate score
    df1=read_post_db(name_db,name_col)
    df_=dfK["result"][0]
    dfJ = json_normalize(df_)
    df_b = pd.merge(dfJ, df1, how= "inner", on= "id")
    df_b['categoryScore'] = np.where(df_b['CorrectAnswers'] == df_b['answers'], 1, 0)
    ef=df_b.groupby('category',as_index=False)[['categoryScore']].agg('sum')
    score = ef["categoryScore"][0]
    scoreP=round(score*100/len(df_),0)
    f=ef.to_json(orient='records')
    data='{"score":'+str(scoreP)+',"result":'+str(f)+'}'
    json_post=json.loads(data)
    #write user into db
    df=[{'name':dfN,'email':dfE,'phone':dfP,'entreprise':dfEN,'score':scoreP, 'category':dfK["result"][0][0]["category"]}]
    mycol.insert_many(df)
    return json_post

