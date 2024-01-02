'''Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''
def string_number(list):
    count =0
    for ele in list:
        if len(ele)>1 and ele[0]==ele[-1]:
            count+=1
    return count
list_ele=input("enter values separate by commas:")
l=list_ele.split(',')
print(string_number(l))
