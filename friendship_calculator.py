your_name=input("Enter your name:")
friend_name=input("Enter your friend's name:")
name_1=your_name.lower()
name_2=friend_name.lower()
name=name_1+name_2
t=name.count('t')
r=name.count('r')
u=name.count('u')
e=name.count('e')
true=t+r+u+e
l=name.count('l')
o=name.count('o')
v=name.count('v')
love=l+o+v+e
total=str(true)+str(love)
print("Love score is:",total)



