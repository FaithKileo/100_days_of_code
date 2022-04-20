# import random
# numbers = random.randint(1, 10)
# decimals = random.random()

# print(numbers)
# print(decimals)

# a = decimals*5
# print(a)

# import random

# numbers = random.randint(0,1)
# if numbers ==1:
#     print("Head")
# else:
#     print("Tail")
    

# # **BILL PAYMENT GAME
# import random
# names = input("Please enter the names each separated by a comma: ")

# names1 = names.split(",")
# # the aim of doing this is to be able to create a list and pick items randomly from it.

# print(names1)

# choosen = random.randint(0 ,len(names1))

# person_who_will_pay = names1[choosen]

# print(f"The person whos is going to pay the bill is {person_who_will_pay}")

                        # OR

# import random
# names = input("Please enter the names each separated by a comma: ")

# names1 = names.split(",")
# print(names1)

# choosen = random.choice(names1)
# print(f"The person whos is going to pay the bill is {choosen}")

# # **MAPPING CHALLENGE

# row1 = ["_","_","_"]
# row2 = ["_","_","_"]
# row3 = ["_","_","*"]

# rows = [row1,row2,row3]
# # print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? ")

# vertical = int(position[1])
# horizontal = int(position[0])

# rows[vertical - 1][horizontal - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")

# # **ROCK, PAPPER & SCISSORS GAME. 
# import random

# items = ["rock", "paper", "scissor"]
# computer_choice = random.randint(0, len(items))

# # print(f"Computer choose: {computer_choice}")

# your_choice = int(input("What is your choice?Tpye 0 for rock,1 for paper and 2 for scissor? "))

# if computer_choice > your_choice:
#     print("You loose")
# elif computer_choice < your_choice:
#     print("You won")
# elif computer_choice == your_choice:
#     print("Draw")
# else:
#     print("Undefined") 






