#blackjack game
#ace will be count as 11 and king,queen and jack will be count as 10, no joker and rest are same
#the deck is unlimited and all cards have the same probability of being chosen
#rules: Get a total close to 21, but not more than 21. if it is higher then you lose
#You get 2 cards
#Dealer also gets 2 cards
#One dealer card is open
#One dealer card is hidden
#You have two main choices:
#Hit 👉 take one more card
#Stand 👉 stop and keep your cards
# You get: Card 1: 10 Card 2: 7 👉 Total = 17 Dealer’s open card:6
# You think: 17 is close to 21,If I take another card, I may go over 21 ,So you choose 👉 Stand
# Dealer shows hidden card.
# Dealer cards: 6 (open) 10 (hidden) 👉 Dealer total = 16
# Rules say:
# Dealer must take a card if total is less than 17
# Dealer takes one more card:
# Gets 8
# 👉 New total = 24
# Dealer has 24 → Bust (more than 21)
# You have 17
# 🎉 You win!
#todo1: create a deal_card() function that uses the list below to *return* a random card. 11 is the ace.
import random as r
import os

def clear():
    os.system('cls')
def deal_card():
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    card = r.choice(cards)
    return card
#todo3:create a function called calculate_score() that takes a list of card as input and returns the score.look sum() to help you do this
def calculate_score(cards):
#inside the calculate_score function check for a blackjack(a hand with only 2 cards ace + 10) and return 0 instead of actual score.0 will represent the blackjack in our game
   #if 11 in cards and 10 in cards and len(cards) == 2:
   if sum(cards) == 21 and len(cards) == 2:
       return 0
   #inside the calculate_score() check for 11 (ace). if the score is already over 21 replace it with 1. use append or remove 
   if 11 in cards and sum(cards) > 21:
       cards.remove(11)
       cards.append(1)      
   return sum(cards)
#todo7:Create a function called compare() and compare the user_score and computer_score. 
# If both are equals then it is a draw.If the user has a blackjack then user is the winner.
# If computer has it,then winner it is.If the user_score/computer_score is above 21 then the user/computer loses it.
# If none of the above, then the player with the highest score is the winner
def compare(user_score,computer_score):
    if user_score == computer_score:
        return "The game is draw"
    elif user_score == 0:
        return "The user has the blackjack. The computer lose"
    elif computer_score == 0:
        return "The computer has the blackjack. The user lose"
    elif user_score > 21:
        return "You went over.You lose"
    elif computer_score > 21:
        return "Computer went over.You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
def play():
    #todo2: deal the user and the computer 2 cards each using the deal_card()
    user_cards=[]
    computer_cards=[]
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    #the score will need to rechecked with every new card that is drawn and check the todo3 till the very end of the game
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"{user_cards} is and user score is {user_score}")
        print(f"{computer_cards[0]}")

        #todo4: call the calculate score(). If the computer or the user has a blackjack(0) or if the user's score is over 21, 
        # then the game ends
        if user_score == 0 or user_score > 21 or computer_score == 0:
            is_game_over = True

        #todo5: If the game has not ended, ask the user if want to draw another cards and if yes then use the deal_card() 
        # function to add another card to user_cards. If no then the game is ended
        else:
            user_should_deal = input("Do you wish to draw another cards. Press yes to continue or no to end\n").lower()
            if user_should_deal == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        #todo6: once the user is done, let the computer play.The computer should draw the card until it is less than 17
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        print(f"You hands {user_cards} and you're score {user_score}")
        print(f"Computer hands is {computer_cards} and computer's score is {computer_score}")
        print(compare(user_score, computer_score))
#todo8:ask the user wants to play another. If 'y' then clear the console and restart the game
while(input("Type 'y' to play another else 'n'")) == 'y':
    clear()
    play()



