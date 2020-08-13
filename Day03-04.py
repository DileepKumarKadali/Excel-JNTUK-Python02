  

# Dictonary

info = {'first_name':'Dileep','last_name':'Kadali','age':34,'city':'Palakollu'}
print('Full Name: ' + info['first_name'] + ' ' + info['last_name'])

# lets say we want more key-value pairs in above dictionary

info['interest'] = 'Coding'
print(info)

# empty dictionary

info2 = {}   # empty dictionary
info2['name'] = 'Parnika'      # adding new key-value pair in an empty dictionary
info2['location'] = 'Valamarru'
print(info2)

# modifying values in ditionary

fruits = {'Yellow':'Apple'}
# lets replace banana with mango
print(fruits)
fruits['Yellow'] = 'mango'
print(fruits)

# removing key-value pairs

info3 = {'first_name':'Dileep','last_name':'Kadali','age':34,'city':'','interest':'Coding'}
print(info3)

del info3['interest']
print('\ndeleting interest field...')
print(info3)

