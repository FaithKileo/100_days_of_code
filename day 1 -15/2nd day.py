# print("Faith"[4])

# # when intergers are treated as a string
# print("123" + "456")

# # when intergers are treated as intergers
# print(123 + 456)

# # converting one data type into another
# length = input("What is your name?\t")
# print(length)

# count = len(length)
# new_count = str( count ) 
# # type conversion.

# print("The length your name is " + new_count + " ,thats simple.")

# # **QUIZ
# numbers = input("Enter the two numbers: ")

# a = int(numbers[0])
# b = int(numbers[1])

# print(a + b) 

# # **CALCULATING BMI OF A PERSON
# weight = input("What is your weight? ")
# height = input("What is your height?")

# BMI = float(weight)/ float (height)**2
# new_BMI = int( BMI )

# print(new_BMI)
# print(round(new_BMI,2)) 

# calc_BMI = new_BMI - 2
# print(calc_BMI)

# # f-string
# print(f"Your considered BMI which is {new_BMI} is perfect.")

# # **AGE REMAIN CALCULATION
# age = input("What is your age? ")

# calc_age = 90 - int(age)
# days = calc_age * 365
# weeks = calc_age * 52
# months = calc_age * 12

# print(f"You have days {days},weeks {weeks},months {months} and {calc_age} years left.")

# # **BILL DISTRIBUTION PROJECT
# print("Welcome to the tip calculator.")
# bill = input("What was the total bill? $")
# percent = input("What percentage tip would you like to give? '10','12', or '15'? ")
# people = input("How many people to split the bill? ")

# new_percent = int (percent) / 100
# new_bill = float(bill) * float(new_percent) + float(bill)
# answer = (new_bill)/ int(people)
# total_bill = (round (answer,2) )

# print(f"Each person should pay ${total_bill}")