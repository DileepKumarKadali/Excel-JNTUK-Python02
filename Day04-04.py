#4)Write a Python Program to display all the UNIQUE elements of the list.

# List
list1 = [10, 20, 10, 30, 40, 40, 10, 20, 30, 50, 40] 
  
# intilize a null list 
unique_list = [] 
      
# Check in all elements 
for x in list1:
    if x not in unique_list: # check if exists in unique_list or not
        unique_list.append(x)

for x in unique_list:
    print (x) 
      
    
  
