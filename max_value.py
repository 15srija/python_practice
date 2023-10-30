list=input("enter the list of numbers separated by comma:")
list_values=list.split(',')
print(list_values)
print("sdadsqwe :::",len(list_values))
# count=0

for c in range(len(list_values)):
    list_values[c]=int(list_values[c])
max_number=list_values[0]
# for i in range(count):
#     if list_values[i]>max_number:
#         max_number=list_values[i]
print(max_number)