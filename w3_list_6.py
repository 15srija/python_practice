'''Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''
def sort_by_last_ele(list):
    sorted_list=[]
    max_ele=list[0][1]
    for i in range(len(list)):
        j=i+1
        for j in range(len(list)):
            if list[i][1]<list[j][1]:
                max_ele=list[i]
                list[i]=list[j]
                list[j]=max_ele
    print("after sorting",list)
list=[]
n=int(input("Enter number of elements in a list"))
for i in range(n):
    tup=input("Enter numbers separated by commas:")
    tuple1=tuple(int(num) for num in tup.split(','))
    list.append(tuple1)
print("before sort:",list)
sort_by_last_ele(list)

