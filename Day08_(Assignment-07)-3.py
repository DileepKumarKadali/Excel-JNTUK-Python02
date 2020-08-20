# import libraries
import pymongo
import json

#connection with db
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dileep789"]
mycol = mydb["dilkk"]

# Read json file
for i in mycol.find():
    if i['city']=='SACRAMENTO':
        print(i)


