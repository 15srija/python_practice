import time
timenow=time.strftime('%H:%M:%S')
print(timenow)
hours=time.strftime("%H")
print(hours)
minutes=time.strftime("%M")
print(minutes)
seconds=time.strftime("%S")
print(seconds)
if(int(hours) < 12):
    print("Good Morning")
elif(int(hours)>=12 and int(hours)<2):
    print("Good Afternoon")
else:
    print("Good Evening")
