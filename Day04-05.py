# 5.Write a Python program to count the number of even and odd numbers from the provided list.


alist = [ 56,34,23,56,4,43,6,7,5,34,5,7645,573,23,6,7,5,4,6,7,5634,3454,345,67,32,45]

even_count=0
odd_count=0

for x in alist:
    if x%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1

print(alist)
print("Total Nubers in List",len(alist))
print("Total Even Nubers in List",even_count)
print("Total Odd Nubers in List",odd_count)
    
