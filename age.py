#WAP to find out how many days, weeks and months
#  left if we live intil 90 years old

age=int(input("Enter your age"))
years_left=90-age
weeks_left=years_left*52
months_left=years_left*12
print(f"There are {years_left*365} days, {weeks_left} weeks and {months_left}  months left if you leave until 90 years.")