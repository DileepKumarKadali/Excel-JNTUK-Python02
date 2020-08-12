#List of Product Details objects
class ProductDetails:
    def __init__(self, productid,productname,price,manfucturername):
        self.productid = productid
        self.productname = productname
        self.price=price
        self.manfucturername=manfucturername
        #print("This is Product  Details constructor")
        
    def met(self):
       return str(self.productid)
       
    def met(self):
        return (str(self.productname))
        
    def met(self):
        return (str(self.price))
        
    def met(self):
        return (str(self.manfucturername))

    def __repr__(self):
        return self.productid+"\t"+str(self.productname)+"\t"+str(self.price)+"\t"+str(self.manfucturername)
        

# Creating list1

list1 = []

# Appending instances to list1
list1.append( ProductDetails("P01", "AAAA", 96,"JNTUK") )
list1.append( ProductDetails("P02", "BBBB", 8,"JNTUK") )
list1.append( ProductDetails("P03", "CCCC", 32,"JNTUK") )
list1.append( ProductDetails("P04", "DDDD", 17,"JNTUK") )

print("\n List-1 Product Details\n-----------------------------------")
for obj in list1:
    print(obj)
    
    
# Product Details sorted with price

list1.sort(key=lambda x: x.price)
print("\n List-1  Product Details sorted with price\n-----------------------------------")
for obj in list1:
    print(obj)



# Product Details Reverse sorted with price

list1.sort(key=lambda x: x.price,reverse=True)
print("\n  List-1 Product Details Reverse sorted with price\n-----------------------------------")
for obj in list1:
    print(obj)

# Product Details display using Iteration

print("\n List-1  Product Details display using Iteration \n-----------------------------------")
for i in range(len(list1)):
               print(list1[i])

#  Create list2, Append and extend with list1 

list2 = []
list2.append( ProductDetails("P11", "XXXX", 96,"JNTUK") )
list2.append( ProductDetails("P12", "YYYY", 8,"JNTUK") )
list2.extend(list1)

print("\n  List-2 Append and Extend \n-----------------------------------")
for obj in list2:
    print(obj)

#  List2 Possitive indexing
print("\n  List-3 Possitive Indexing for List-2 \n-----------------------------------")
list3=list2[:2]
for obj in list3:
    print(obj)

#  List2 Nagative indexing
print("\n  List-4 Negative Indexing for List-2 \n-----------------------------------")
list4=list2[:-3]
for obj in list4:
    print(obj)


#  List2 Nagative indexing
print("\n  List-4 Negative Indexing for List-2 \n-----------------------------------")
list5=list2[-3:]
for obj in list5:
    print(obj)

    
print("-------------------------------------\n")
list1.append( ProductDetails("P05", "EEEE", 62,"JNTUK") )
list1.append( ProductDetails("P06", "FFFF", 43,"JNTUK") )
list2.append( ProductDetails("P13", "ZZZZ", 37,"JNTUK") )
              
list6 = set(list2)-set(list1)
for obj in list6:
    print(obj)


