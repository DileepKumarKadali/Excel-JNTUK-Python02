
#count the number of characters
str1="Dileep Kumar Kadali"
dict = {}
for n in str1:
    keys = dict.keys()
    if n in keys:
       dict[n] += 1
    else:
       dict[n] = 1
    
print(dict)
