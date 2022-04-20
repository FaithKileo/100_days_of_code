import random

attempts1 = 10
attempts2 = 5

def game(guess, number, attempts):
    """ Compares users guess against number and returns the number of attempts left."""

    if guess < number:
        print("Too low")
        return attempts - 1
    
    elif guess > number:
        print("Too high")
        return attempts - 1
        
    else:
        print(f"Congratulation you got it right the answer is {number}")

def user_level():
    user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if user_choice == "easy":
        return attempts1
       
    elif user_choice == "hard":
        return attempts2

    else:
        return "Invalid input"
        
def gameone():       
    print("WELCOME TO THE NUMBER GUESSING GAME.")

    number = random.randint(1, 100)
    print("Am thinking of a number between 1 and 100.")
    print(number)
    
    attempts = user_level()
    
    guess = 0
    while guess != number:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        attempts = game(guess, number, attempts)
        if attempts == 0:
            print("You have run out of guesses. You loose")
            return

gameone()    



