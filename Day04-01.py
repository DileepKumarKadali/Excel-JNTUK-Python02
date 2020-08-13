#1)Write a Python program to count the number of characters (character frequency) in a string

mystr = "Dileep Kumar Kadali"

freq_char = {} 
  
for char in mystr: 
    freq_char[char] = freq_char.get(char, 0) + 1


print (str(freq_char))
