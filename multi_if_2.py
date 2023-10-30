'''pizza order progeam
small pizza=100
medium pizza=200
large pizza=300
pepper for small pizza: 30
pepper for medium or large pizza: 50
extra cheese for any size pizza: 20'''
order_pizza=input("Do you want to order pizza:y/n")
bill=0
if order_pizza == 'y' or order_pizza=='Y':
    size=input("Small/medium/large(s/m/l):")
    if size=='s':
        bill+=100
        print("cost Rs 100")
    elif size=='m':
        bill+=200
        print("cost Rs 200")
    elif size=='l':
        bill+=300
        print("cost Rs 300")
    pepper=input("want pepper on it(y/n):")
    if pepper=='y':
        if size=='s':
            bill+=30
        else:
            bill+=50
    cheese=input("Want xtra cheese(y/n):")
    if cheese=='y':
        print(f"total amount:{bill+20}")




