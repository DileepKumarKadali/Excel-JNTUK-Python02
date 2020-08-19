import os

# files & directories of the current directory
 
files = os.listdir()
 
# if you wish the display of files of different directory
#files = os.listdir(path of the directory)
 
for file in files:
    if os.path.isfile(file):
        file = file.strip()
        print(file)

