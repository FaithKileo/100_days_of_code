stu_height = input("Enter the height of each student please:")
stu_height = stu_height.split()

for height in range (0, len(stu_height)):
    stu_height[height] = int(stu_height[height])
print(stu_height)

answer = 0
for height in stu_height:
    answer = answer + height   
print (answer)

average = answer/ len(stu_height)

print(round(average))

stu_height = input("Enter the height of each student please:")
stu_height = stu_height.split()

for height in range (0, len(stu_height)):
    stu_height[height] = int(stu_height[height])
print(stu_height)

highest_height = 0
for height in stu_height:
    if height > highest_height:
        highest_height = height
print(height)

# even_total=0
# for number in range(1, 101, 2):
#     even_total = even_total + number
# print(even_total)

# for number in range(1, 101):
    
#     if number%5 == 0 and number%3 == 0:
#         print("FizzBuzz")
        
#     elif number%5 ==0:
#         print("Buzz")
        
#     elif number%3 == 0:
#         print("Fizz")
        
#     else:
#         print(number)

# # PASSWORD GENERATOR PROJECT
# import random

# letters = ['a','b','c','d','e','f','g','h','i','j','k','l']
# numbers = ['1','2','3','4','5','6','7','8','9']
# symbols = ['@','#','$','$','&','*','^']

# print("WELCOME TO THE PYPASSWORD GENERATOR.")

# p_letters = int(input("How many letters would you like?: \n"))
# p_numbers = int(input("How many numbers would like?: \n"))
# p_symbols = int(input("How many symbols would you like? \n"))

# password = " "

# for letter in range(1, p_letters + 1): 
       
#        codeletter = random.choice(letters)
#        password += codeletter

# # password1 = " "

# for number in range(1, p_numbers + 1): 
       
#        codenumber = random.choice(numbers)
#        password += codenumber

# # password2 = " "

# for symbol in range(1, p_symbols + 1): 
       
#        codesymbol = random.choice(symbols)
#        password += codesymbol

# print(f"This is your password: {password}")