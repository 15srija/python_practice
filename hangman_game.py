import random
import hangman_stages
print("Let's play hangman game!!")
words_list=['apple','mangoes','banana','watermelon','muskmelon','pen','pencil','book']
word=random.choice(words_list)
guess_word=[]
lives=6
length=len(word)
for i in range(length):
    guess_word.append('_')
print(guess_word)
game_over=False
while not game_over:
    string1=input("Enter the letter:")
    for i in range(length):
        letter=word[i]
        if letter==string1:
            guess_word[i]=string1
    print(guess_word)
    if string1 not in word:
        lives=lives-1
        print("No Match")
        if lives==0:
            game_over=True
            print("You Lose!")
    if '_' not in guess_word:
        game_over=True
        print("You WIN!!")
    print(hangman_stages.stages[lives])

