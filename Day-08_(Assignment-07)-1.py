# import libraries
import pymongo
import json

#connection with db
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dileep789"]
mycol = mydb["dilkk"]

# Read json file
with open('realestate.json')  as rdata:
      mydata = json.load(rdata) 


# inserting all the records
ob = mycol.insert_many(mydata)
print(mydata)



# Display
for ob in mycol.find():
    print(ob)
    print("_____________________")

