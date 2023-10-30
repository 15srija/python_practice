# Python | Count occurrences of an element in a list without using count()

list=input("enter the values separated by comma:")
list=list.split(',')
length=len(list)
ele=input("enter the element to count it's occurances:")
count=0
for i in range(length):
    if ele==list[i]:
        count+=1
print(ele,"has occurred",count,"times in the list")