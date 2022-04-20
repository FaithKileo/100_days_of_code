# THE LONG FORM OF THE WORD *args IS arguments

# def add(*args):
#     sum = 0
    
#     for n in args:
#         sum += n
#     return sum  
        
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9)) 

# THE LONG FORM OF THE WORD **kwargs is KEY WORD ARGUMENTS 

# def calculate(**kwargs):
#     print(kwargs)
    
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # # above separate each item in a dict to its own 
    
# calculate(add = 3, multiply = 5) 
# # this creates a dictionary 

        #    OR,... when we want to get hold of an item and work with it 
        
# def calculate(n, **kwargs):
#     print(kwargs) 
    
#     n += kwargs["add"] 
#     n *= kwargs["multiply"] 
    
#     print(n)
    
# calculate(2, add = 3, multiply = 5) 

class Car:
    
    def __init__(self, **kwargs):
        self.make = kwargs["make"] 
        self.model = kwargs["model"] 
        
my_car = Car(make = "Nissan", model = "GT-R") 
print(my_car.make) 
print(my_car.model)