# LIST COMPREHENSION 

# numbers = [1, 2 , 3] 
# new_numbers = [ n+1 for n in numbers ] 
# print(new_numbers) 

# name = "Faith" 
# new_name = [letter for letter in name] 
# print(new_name) 

# numbers = range(1, 5) 
# new_num = [ n*n for n in numbers ]  
# print(new_num)

# names = [ "Faith", "Angela", "Catty", "Ann", "Andy"] 
# long_names = [ name.upper() for name in names if len(name) > 4 ] 
# print(long_names) 

# numbers = [ 1, 2, 3, 5, 8, 13, 21, 34, 55 ] 
# even_nums = [num for num in numbers if num % 2 == 0] 
# print(even_nums)    


# # DICTIONARY COMPREHENSION 
# import random 

# names = [ "Faith", "Angela", "Catty", "Ann", "Andy"]

# student_scores = { student:random.randint(1, 100) for student in names } 
# print(student_scores) 

# passed_students = { student:score for (student, score) in student_scores.items() if score > 60 } 
# print(passed_students) 

# # QUIZ 

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?" 

# # for word in sentence.split():
# #     print(word) 

# result = {word:len(word) for word in sentence.split()} 
# print(result) 

# QUIZ 2 
weather_C = {
    "Monday":12 ,
    "Tuesday": 14,
    "Wensday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday":24,
} 

weather_F = {day: ((temp_c * 9/5) + 32)  for (day, temp_c) in weather_C.items() } 
print(weather_F)