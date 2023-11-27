import random
import logo2
import project_database
# print(logo2.logo)
def account_details(account):
    name=account['name']
    country=account['country']
    return f"{name}, from {country}"

compare1=random.choice(project_database.data)
compare2=random.choice(project_database.data)
print(f"compare-1: {account_details(compare1)}\n {logo2.vs}\n compare2:{account_details(compare2)}")
choice=int(input("Who has More followers: 1 or 2\n"))
if choice==1 and compare1['follower_count']>compare2['follower_count']:
    score=score+1
    print(score)
elif choice==2 and compare2['follower_count']>compare1['follower_count']:
    score=score+1
    print(score)
else:
    print("You lose the game.")
    print(score)
