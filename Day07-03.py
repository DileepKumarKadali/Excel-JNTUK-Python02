
import os
import sys
import datetime



#print("My Current UserName: ",os.getuid())
print("My Current Working Directory: ",os.getcwd())
#print("My Operating System: ",os.uname())
print("My Current Ruuning Programs: ",os.popen('wmic process get description, processid').read())
print("My Current Timestamp: ",datetime.datetime.now().timestamp())

today = datetime.date.today()
print("Today Date: ",today)
print("Yesterday Date: ",today - datetime.timedelta(days=1))
print("Tomorrows Date: ",today + datetime.timedelta(days=1))
print("All the environment variables that are existing ",os.environ.items())
print("My python Executable path: ",sys.executable)
