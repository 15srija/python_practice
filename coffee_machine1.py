resources={
    'milk': 500,
    'coffee':250,
    'water':500
}

menu={
    
}
is_on=True
while is_on:
    coffee_type=input("Enter the type of coffee type you want(lattee/expresso/capuccino):")
    if coffee_type=='off':
        is_on=False
    elif coffee_type=='report':
        print(f"Milk:{resources['milk']}ml\nCoffee:{resources['coffee']}g\nWater:{resources['water']}ml")
    else:
