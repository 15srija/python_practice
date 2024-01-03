import numpy as np

a=np.array(10)
print(a)
b=np.array([10,20,30])
print(b)
c=np.array([[1,2,3],[2,3,4],[3,4,5]])
print(c)
d=np.array([[[1,2,3],[2,3,4]],[[2,3,4],[3,4,5]]])
print(d)

l=[[5,6,7],[1,2,3]]
print("List is :",l)
al=np.asarray(l,int,'F')
print(al)
