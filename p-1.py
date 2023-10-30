# Python program to interchange first and last elements in a list

list=input("enter the elements with space")
list=list.split(' ')
size=len(list)
temp=list[0]
list[0]=list[size-1]
list[size-1]=temp
print("list after interchanging 1st and last elements in the list are:")
print(list)
