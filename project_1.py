import random
import logo_art
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level):
    if level=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
def check_answer(guess,answer,attempts):
    if guess<answer:
        print("You are too low")
        return attempts-1
    elif guess>answer:
        print("You are to high")
        return attempts-1
    else:
        print(f"Your guess is right")

def game(): 
    print(logo_art.logo)   
    print("Let me think of a number from 1 to 50.")
    answer=random.randint(1,50)
    level=input("Choose level of difficulty...Type 'easy' or 'hard':")
    attempts=set_difficulty(level)
    guess=0
    while guess!=answer:
     print(f"You have {attempts} remaining to guess the number")
     guess=int(input("Guess a number:"))
     attempts=check_answer(guess,answer,attempts)
     if attempts==0:
         print("You are out if guesses....You lose!")
         return
     elif guess!=answer:
         print("Guess again!")
game()