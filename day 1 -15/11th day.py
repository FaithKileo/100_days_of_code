import random

def deal_card():
    """Takes any card randomly and prints it out"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards) 
    return card 
game_over = False

user_card = []
computer_card = []

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
    
print(user_card)
print(computer_card)

def calculate_score(cards):
    """Takes the list of each card for user and computer and adds them"""
    return sum(cards)

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # this is called a blackjack, where the user or computer can win with the blackjack
    
    if sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
print(calculate_score(user_card))
print(calculate_score(computer_card))
 
if sum(computer_card) == 21 or sum(user_card) == 21 or sum(user_card) > 21:
    game_over = True 
    
if not game_over:
    choice = input(print("Do you want to add another card? Type 'y' or 'n':"))
    if choice == "y":
        calculate_score(user_card).append(deal_card())
else:
    game_over = True 