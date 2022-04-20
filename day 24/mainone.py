# this is a way of reading the text
with open("day 24\my_file.txt") as file:
    contents = file.read()
    print(contents)  
    
# # a stands for append
# with open("day 24\my_file.txt", mode= "a") as file:
#         file.write("\n new text")
    
# # a way of writting something in a text 
# with open("day 24\my_file.txt", mode= "w") as file:
#     file.write("New text")