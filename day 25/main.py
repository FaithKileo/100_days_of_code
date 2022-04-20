# with open("day 25\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data) 
# # as you can see the process above, in its list form it has got alot of 
# # complications and cleaning so lets look for another alternative. 

# import csv 

# with open("day 25\weather_data.csv") as data_file:
#     data = csv.reader(data_file) 
#     # print(data) 
    
#     temperatures = []
    
#     for row in data:
#         # print(row)
        
#         # if you want to get hold of a certain column then you write, eg
#         # print(row[1]) 
        
#         # getting hold of the temperatures but without the title temp
#         if row[1] != "temp":
#             temperatures.append(row[1])
            
#     # the list of the temperatures allows us now to work with it as intergers.
#     print(temperatures) 

import pandas
import pathlib

current_dir = pathlib.Path(__file__).parent
#print(current_dir)

data = pandas.read_csv(current_dir / "weather_data.csv")
print(data)



