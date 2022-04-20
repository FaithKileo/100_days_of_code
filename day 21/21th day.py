# CLASS INHERITANCE 

class Fish: 
    
    def __init__(self):
        self.eyes = 2 
        
    def breathe(self):
        print("Inhale, Exhale") 
        
# fish = Fish()
# print(fish.eyes) 
# fish.breathe()
            
class Animal(Fish): 
    
    def __init__(self): 
        super().__init__()
        
    def breathe(self):
        super().breathe()
        print("doing this under water.")    
    # we have modified the breathe method in the Animal class 
        
    def swim(self):
        print("Moving in water.")
        
nimo = Animal() 
nimo.swim() 
nimo.breathe() 
print(nimo.eyes)  

# as you can see above all this which can be done inside the Fish class can also be performed
# inside the animal class and that is what is called class inheritance.