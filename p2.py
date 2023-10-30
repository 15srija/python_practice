list=input("Enter the elements into the list:")
list=list.split(' ')
n1=int(input("enter the position1 to swap the element:"))
n2=int(input("enter the position2 to swap the element:"))
temp=list[n1]
list[n1]=list[n2]
list[n2]=temp
print("list after the elements are swapped:")
print(list)