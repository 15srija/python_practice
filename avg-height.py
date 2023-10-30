heights=input("enter heights with spaces:")
height_list=heights.split(' ')
count=0
sum=0
for i in height_list:
    count=count+1
for height in range(count):
    height_list[height]=int(height_list[height])
    sum=sum+height_list[height]
avg=round(sum/count)
print("average height is:",avg)