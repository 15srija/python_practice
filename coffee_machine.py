Menu={
   "latte":{
      "ingredients":{
         "water":100,
         "milk":150,
         "coffee":24
      },
      "cost":150
   },
   "espresso":{
      "ingredients":{
         "water":150,
         "milk":200,
         "coffee":30
      },
      "cost":200
   },
   "cappuccino":{
      "ingredients":{
         "water":100,
         "milk":200,
         "coffee":40
      },
      "cost":300
   }
}
profit=0
resourses={
    "water":500,
    "milk":200,
    "coffee":100,
}


def check_resources(order_ingredients):
   for item in order_ingredients:
      if order_ingredients[item]>resourses[item]:
         print(f"Soory there is not enough {item}")
         return False
   return True

def process_coins():
   total=0
   print("Please enter coins:")
   coins_five=int(input("How many 5rs coins?:"))
   coins_ten=int(input("How many 10rs coins?:"))
   coins_twenty=int(input("How many 20rs coins?:"))
   total=(coins_five*5) + (coins_ten*10) + (coins_twenty*20)
   return total

def is_payment_successfull(money_recieved,coffee_cost):
   if money_recieved>=coffee_cost:
      global profit
      profit=profit+coffee_cost
      change=money_recieved-coffee_cost
      print(f"Here is your Rs{change} in change.")
      return True
   else:
      print("You have insufficent money! Money refunded")
      return False

def make_coffee(coffee_type, coffee_ingredients):
   global resourses
   for item in coffee_ingredients:
      resourses[item]-=coffee_ingredients[item]
   print(f"Here is your {coffee_type}..!Enjoy!!")

def refill_coffee():
   for item in resourses:
      resourses[item]+=250
    
is_on=True
while is_on:
 choice=input("What would you like to have?(latte/espresso/cappuccino):")
 if choice=="off":
     is_on=False
 elif choice=="report":
    print(f"Water={resourses['water']}ml\nMilk={resourses['milk']}ml\nCoffee Beans={resourses['coffee']}g\nCoins Left=rs{profit}")
 elif choice=="refill":
    refill_coffee()
 else:
    coffee_type=Menu[choice]
    print(coffee_type)
    if check_resources(coffee_type['ingredients']):
       payment=process_coins()
       if is_payment_successfull(payment,coffee_type['cost']):
          make_coffee(choice,coffee_type['ingredients'])