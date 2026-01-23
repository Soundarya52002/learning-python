#todo1 : display art
from art import logo,vs
from game_data import data
import random as r
import os
def clear():
    os.system('cls')
print(logo)
def checking(guess,a_follower_count,b_followe_count):
    if a_follower_count > b_follower_count:
        return guess == 'a'
    else:
        return guess == 'b'
score = 0
game_should_end = True
account_b = r.choice(data)
#todo3 : format the account data to printable
while game_should_end:
    def account_info(account):
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]
        return (f"{account_name}, a {account_description} from {account_country}")

    #todo2 : generate random account for the game
    account_a = account_b
    account_b = r.choice(data)
    while account_a == account_b:
        account_b = r.choice(data)
    print(f"Compare a : {account_info(account_a)}." )
    print(vs)
    print(f"Compare b : {account_info(account_b)}.")
    #todo4 : ask the user a or b
    guess = input("Type your answer 'A' or 'B': ").lower()
    #todo5 : check if it is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_check_correct = checking(guess, a_follower_count,b_follower_count)
    clear()
    print(logo)
    #todo6 : give user the feedback
    #todo7 : score keeping
    if is_check_correct:
        score += 1
        print(f"You're correct! and your score is {score}")
    else:
        game_should_end =False
        print(f"Sorry! you are wrong and your final score is {score}")

    #todo8 : make the game repeatable
    #todo9 : make the account b as account a for next step
    #todo10 : clear the screen