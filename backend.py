from pymongo import MongoClient
from config import *
from datetime import datetime

# cluster = MongoClient("mongodb+srv://AshwinSolankiBoss:"+pswd+"@mydatabase.9snxp.mongodb.net/"+dbname+"?retryWrites=true&w=majority")
# db=cluster[dbname]
# Collection=db[coll]

post={
    "isNote":True,
    "Username":"AshwinSolanki",
    "Title":"Ashwin Solanki",
    "Date": str(datetime.now().date()),
    "Time": str(datetime.now().time()),
    "Note":20
}

def AddUser(username,password):
    cluster=MongoClient("mongodb+srv://AshwinSolankiBoss:"+pswd+"@mydatabase.9snxp.mongodb.net/"+dbname+"?retryWrites=true&w=majority")
    db=cluster[dbname]
    Collection=db[coll]
    if not Collection.find_one({'IsCred':True,"Username":username}):
        Collection.insert_one({"IsCred":True,"Username":username,"Password":password})
        return True
    return False

def IsUser(username,password):
    cluster=MongoClient("mongodb+srv://AshwinSolankiBoss:"+pswd+"@mydatabase.9snxp.mongodb.net/"+dbname+"?retryWrites=true&w=majority")
    db=cluster[dbname]
    Collection=db[coll]
    return bool(Collection.find_one({"IsCred":True,"Username":username,"Password":password}))
