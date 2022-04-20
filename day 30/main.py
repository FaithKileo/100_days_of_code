try:
    # this is a file not found error
    file = open("file.txt") 
    dictionary = {"key": "value"}
    print(dictionary["key"])
    
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("something") 
    
except KeyError as error_message:
    print(f"That key {error_message} does not exists") 
    
else:
    content = file.read() 
    print(content) 
    
finally:
    raise KeyError() 

# When do we raise
height = int(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("The human height should not be over 3 meters.")
    
bmi = weight/ height**2
print(bmi) 
