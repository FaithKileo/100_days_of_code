# def format_name(f_name, l_name):

#     print(f_name.title())
#     print(l_name.title())

# format_name("faith", "FRANK")

# def format_name(f_name, l_name):
#     """title() converts every first later of any word or sentence to capital letter"""
    
#     if f_name == "" or l_name == "":
#         return "Please fill in the information"
    
#     new_f_name = f_name.title()
#     new_l_name = l_name.title()
    
#     return f"{new_f_name} {new_l_name}"
    
# name1 = input("Enter your first name")
# name2 = input("Enter your second name")

# print(format_name( name1, name2 ))

# def is_leap( year):
#     """Takes in the year and identify it wether it is leap or not """

#     if year%4 == 0:
#         if year%100 != 0:
#             if year%400 != 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True 
#     else:
#         return False
    
# def days_in_month(year, month):
#     """ Takes in the year and the month and identify it wether leap or not and returns the number of days in the month"""
    
#     if month > 12 or month < 1:
#         return "Invalid input"
#     month_days = [ 31, 28, 31, 30, 31, 31, 30]
    
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month -1]
    
# year = int(input("Enter the year you want to check: "))
# month = int(input("Enter the month you want to check: "))
# days = days_in_month(year, month)

# print(days)


# # CALCULATOR PROJECT
# def add(n1, n2):
#     answer = n1 + n2
#     return answer

# def substraction(n1, n2):
#     answer = n1 - n2
#     return answer

# def multiplication(n1, n2):
#     answer = n1*n2
#     return answer

# def division(n1, n2):
#     answer = n1/n2
#     return answer
    
# dictionary = {
#     "+" : add,
#     "-" : substraction,
#     "*" : multiplication,
#     "/" : division,
# }

# n1 = int (input("Enter the first number: "))
# n2 = int (input("Enter the second number: "))

# for symbol in dictionary:
#     print(symbol)
    
# operation_symbol = input("Choose an operation symbol: ")

# calculation_function = dictionary[operation_symbol]
# answer = calculation_function(n1, n2)

# print(f"{n1} {operation_symbol} {n2} = {answer}")
