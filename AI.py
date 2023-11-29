import random
#### sample practice for python##############
while(True):
    user_choice=int(input("Enter your choice 0 for rock, 1 for paper, 2 for scissors\n"))
    computer_choice=random.randint(0,2)
    print("Computer Choice:",computer_choice)
    if computer_choice == user_choice:
        print("Draw Match!!!")
    elif computer_choice==2 and user_choice==0:
        print("You lose!")
    elif user_choice==2 and computer_choice:
        print("You Won!!")
    elif computer_choice>user_choice:
        print("You Lose!")
    elif user_choice>computer_choice:
        print("You Win!")
