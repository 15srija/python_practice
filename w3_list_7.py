'''Write a Python program to remove duplicates from a list.'''
def remove_dupli(list):
    for ele in list:
        if list.count(ele)>1:
            ''''logic missing'''
    return list

list=input("Enter elements separated by comma:")
list1=list.split(',')
print(list1)
remove_dupli(list1)
