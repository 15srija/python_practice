a=1
b=2
c=4
for c in range(4,7):
    b=(c+11)&a
    if ((b+6)>(c-b)):
        continue
    else:
        break
    b=c+b
print (a+b)