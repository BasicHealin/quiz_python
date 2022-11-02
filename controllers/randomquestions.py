import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
import flask
from flask import request, jsonify
import json 
import pandas as pd


def randomquestions(category,n,df):
    
    df1=df.loc[df.category== category]
    df1=df1.sample(n)
    return(df1)
def getcategory(df):
    cat=df.groupby("category").agg(['unique'])
    l=[]
    for row in cat.iterrows():
        l.append(row[0])
    return l
