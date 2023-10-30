Your_name=input("Enter your name:")
friend_name=input("Enter your friend's name:")
name1=Your_name.replace(" ","")
name2=friend_name.replace(" ","")
for i in name1:
    for j in name2:
        if i==j:
           name1=name1.replace(j,"",1)
           name2=name2.replace(j,"",1)
           break 
count=len(name1+name2)

if count>0:
     list = ['Friends','Lovers','Attraction','Marriage','Enemies','Siblings']
     while len(list)>1:
         c=count%len(list)
         index=c-1
         if index>=0:
             left=list[:index]
             right=list[index+1:]
             list=right+left
         else:
             list=list[:len(list)-1]
     print("Relationship is:",list[0])

             