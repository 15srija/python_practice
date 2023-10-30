list1=[1,1,1]
list2=[1,1,1]
list3=[1,1,1]
final_list=[list1,list2,list3]
print(final_list)
x=int(input(print("enter row number to hide money:")))
y=int(input(print("enter column number to hide:")))
final_list[x][y]=0
print(final_list)