# HANGMAN GAME
import random

end_of_game =False
lives = 6

words = ["catty", "cable", "nurse", "asprin", "chair"]
chosen_word = random.choice(words)
# print(chosen_word)
            
display = []
for _ in range(len(chosen_word)):
    display += "_"    

while not end_of_game:
            
    guess = input("Enter your guess: ")
    corr_guess = guess.lower()     
            
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess: 
            display[position] = letter
        else:
            print("No match")
            
    if guess not in chosen_word:
        lives -=1
        
        if lives == 0:
           end_of_game = True
           print("You loose.")
           
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win")

        