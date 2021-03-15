from pymongo import MongoClient
from datetime import datetime
import os
from boto.s3.connection import S3Connection

link = S3Connection(os.environ['MONGODB_URI'])

post={
    "isNote":True,
    "Username":"AshwinSolanki",
    "Title":"Ashwin Solanki",
    "Date": str(datetime.now().date()),
    "Time": str(datetime.now().time()),
    "Note":20
}

def AddUser(username,password):
    cluster=MongoClient(link)
    db=cluster['Book']
    Collection=db['Page']
    if not Collection.find_one({'IsCred':True,"Username":username}):
        Collection.insert_one({"IsCred":True,"Username":username,"Password":password})
        return True
    return False

def IsUser(username,password):
    cluster=MongoClient(link)
    db=cluster['Book']
    Collection=db['Page']
    return bool(Collection.find_one({"IsCred":True,"Username":username,"Password":password}))