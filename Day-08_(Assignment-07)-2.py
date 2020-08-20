# import libraries
import pymongo
import json

#connection with db
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dileep789"]
mycol = mydb["dilkk"]

# Read json file
with open('realestate1.csv',"w")  as mydata:
    writer = csv.writer(mydata)
    for x in mycol.find():
        t=[i for i in x.keys()]        
        writer.writerow(t[1:])
        break
    for x in mycol.find():
        t=[i for i in x.values()]        
        writer.writerow(t[1:])


