# Write a Python program that accepts a sequence 
# of comma-separated numbers from the user 
# and generates a list and a tuple of those numbers.

values=input("Enter the values:")
values=values.split(' ')
print(values)
print(tuple(values))