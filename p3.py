list=input("enter the values separat them with comma:")
list=list.split(',')
for i in range(len(list)):
    list[i]=int(list[i])
print(list)
print("List after reversing:")
# list.reverse()
# print(list)
length=len(list)-1
list2=[]
for i in range(len(list)):
    list2.append(list[length-i])
print(list2)