# 7) Write a Python program to display all the odd numbers from 20 to 10


#Method-1
for i in reversed(range(11,20,2)) :
    print(i,end=",")
print("\n")
#Method-2
for i in reversed(range(11,20)) :
    if i%2==1:
        print(i,end=",")
