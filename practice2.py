import random
names=input("Enter Names of your freinds:")
n_list=names.split(",")
print(n_list)
length=len(n_list)
index=random.randint(0,length)
person=n_list[index]
print(f"{person} have to pay the bill")