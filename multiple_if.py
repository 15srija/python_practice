# roller coaster program
height=int(input("Enter Height:"))
bill=0
if height>3:
    print("can ride")
    age=int(input("Enter your age:"))
    if age<12:
        bill=150
        print("Ticket price is Rs.150")
    elif age >12 and age<=18:
        bill=250
        print("Ticket price is Rs.250")
    else:
        bill=500
        print("Ticket price is Rs.500")
    photo=input("Want a photo y/n:")
    if photo == 'y' or photo == 'Y':
        bill=bill+50
        print(f"Total price is {bill}")
 