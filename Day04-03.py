# 3)write an conditional statement to find biggest number in 3 numbers.


n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

max=n1

if (n2>max):
   max = n2
if (n3>max):
   max = n3

 
print("The largest number is",max)
