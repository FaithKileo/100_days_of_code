# height = float(input("Enter your height please: "))
# bill = 0

# if height>120:
#     print("You can ride")
#     age = int(input("enter your age please: "))
    
#     if age<12:
#         bill = 5
#         print("You have to pay $5")
#     elif age>12 & age<18:
#         bill = 7
#         print("You have to pay $7")
#     else:
#         bill = 12
#         print("You have to pay $12")
      
#     photo = input("Do you want a photo taken? Type Y or N ")    
#     if photo == "Y":
#         bill = bill +3
#     else:
#         print(f"Your total bill is {bill}")
        
# else:
#     print("Sorry you are still short.")

# # **EVEN OR ODD
# number = int(input("Enter the number please: "))
# if number%2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# # **CALCULATING BMI. 
# weight = int(input("Enter your weight please in kg: "))
# height = int(input("Enter your height please in cm:"))

# BMI = (weight)/(height)**2

# if BMI<18:
#     print(f"Your bmi is {BMI} ,you are underweight")
# elif BMI>18 & BMI<25:
#     print(f"Your bmi is {BMI} ,you have normal weight")
# elif BMI>25 & BMI<30:
#     print(f"Your bmi is {BMI} , you have overweight")
# elif BMI>30 & BMI<35:
#     printf(f"Your bmi is {BMI} ,you have obesity")
# else:
#     print(f"Your bmi is {BMI} , you have clinically obese")

# # **LEAP YEAR CHECKING
# year = int(input("Enter the year you want to check:"))

# if year%4 == 0:
#     if year%100 != 0:
#         if year%400 != 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Not leap year")
# else:
#     print("Not leap year")

# print("WELCOME TO THE PIZZA DELIVERY")

# bill = 0
# size = input("What size of pizza do you want? Type S,M or L: ")
# perperoni = input("Do you want some perperoni? Tpye Y or N: ")
# extra_cheese = input("Do you want some extra cheese? Type Y or N: ")

# if size== "S":
#     bill = bill + 15
#     if perperoni == "Y":
#         bill += 2
#     else:
#         print(f"Your total bill is {bill} ")
    
# elif size== "M":
#     bill = bill + 20
#     if perperoni == "Y":
#         bill += 3
#     else:
#         print(f"Your total bill is {bill} ")    
    
# else:
#     bill = bill + 25      
#     if perperoni == "Y":
#         bill += 3
#     else:
#         print(f"Your total bill is {bill} ") 
        
# if extra_cheese == "Y":
#     bill += 1
#     print(f"Your total bill is {bill} ")
# else:
#     print(f"Your total bill is {bill} ")   

# print("WELCOME TO THE LOVE CALCULATOR.")

# name1 = input("What is your name? ")
# name2 = input("What is the other name? ")

# combined_names = name1 + name2

# new_name = combined_names.lower()


# T = new_name.count("t")
# R = new_name.count("r")
# U = new_name.count("u")
# E = new_name.count("e")

# L = new_name.count("l")
# O = new_name.count("o")
# V = new_name.count("v")
# E = new_name.count("e")

# score1 = (T + R + U + E)
# score2 = (L + O + V + E)

# new_score1 = str(score1)
# new_score2 = str(score2)

# love_score = (new_score1 + new_score2)

# print(f"Your score is {love_score}")

# love1_score = int(love_score)

# if love1_score<10 & love1_score>90:
#     print("You go together like coke and mentos")
# elif love1_score>=40 & love1_score<=50:
#     print("You are alright together.")
# else:
#     print("Not so sure about you two.")


# print("WELCOME TO THE TREASURE ISLAND.\n Your mission is to find the treasure.")

# direction = input("Where do you want to go? Type 'left' or 'right' ")

# if direction == "left":
#     choice = input("Do you want to swim or wait? ")
    
#     if choice == "wait":
#         door = input("Which door do you want to go through? red,blue or yellow? ")
        
#         if door == "yellow":
#             print("You have won. Congatulations")
#         else:
#             print("Game over.")
#     else:
#         print("Game over.")
    
# else:
#     print("Game over.")

