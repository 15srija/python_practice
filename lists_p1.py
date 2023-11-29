# reverse a list
list1=[10,20,30,40]
list1.reverse()
print(list1)

# list concatination
l1=["M","na","i","ke"]
l2=["y","me","s","lly"]
l3= [i+j for i,j in zip(l1,l2)]
print(l3)

# turn every item of list iinto its square

l1=[10,20,30]
l2=[]
for i in l1:
    l2.append(i**2)
print(l2)

