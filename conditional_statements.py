weight=float(input("Enter weight:"))
height=float(input("Enter height:"))
BMI=round(weight/(height**2))
if BMI<18.5:
    print(f"Your BMI is {BMI} and you are underweight")
elif BMI>18.5 and BMI<24.5:
    print((f"Your BMI is {BMI} and you are normal weight"))
elif BMI>25:
    print("you are over weight")
