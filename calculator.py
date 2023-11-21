def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operators={
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide,
    }
def calculator():
    num1=int(input("Enter 1st number:\n"))
    for symbol in operators:
        print(symbol)
    
    continue_flag=True
    while continue_flag:
       op_symbol=input("Pick an Operation:")
       num2=int(input("Enter 2nd symbol:\n"))
       calculator_func=operators[op_symbol]
       output=calculator_func(num1,num2)
       print(f"{num1} {op_symbol} {num2} = {output}")
       
       calculate_again=input(f"Enter 'y' to continue calculation with {output} or 'n' to calculate with inputs or 'e' to exit.\n")
       if calculate_again=='y':
           num1=output
       elif calculate_again=='n':
           calculator() 
       elif calculate_again=='e':
           continue_flag=False
           print("Exit from the calculation")

calculator()