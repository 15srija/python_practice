def days_in_month(year,month):
 if month==2:
     if year%4==0:
       if year%100==0:
           if year%400==0:
             return 29
           else:
            return 28
       else:
          return 29
     else:
       return 29
 elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    return 31
 else:
    return 30

year=int(input("Enter Year:"))
month=int(input("Enter month number..1 for jan, 2 for feb and so on:"))
print(f"There are {days_in_month(year,month)} in the month of {month} in the year {year}")