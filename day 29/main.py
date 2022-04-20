from tkinter import *
from tkinter import messagebox
import random
import json 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(password_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(password_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input3.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_input1.get() 
    email = email_input2.get() 
    password = password_input3.get() 
    new_data = {
        website: {
            "email": email, 
            "password": password,
        }
    }
    
try:
    with open("data.json", "r") as data_file:
        # json.dump(new_data, data_file, indent= 4)

        # reading the old data
        data = json.load(data_file)  
        
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent= 4) 
        
        # updating the old data with a new data. 
        data.update(new_data)  
        
        # writting and saving the new data into the old data.
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent= 4)
            
        # deleting the entries on the screen after their entry 
        website_input1.delete(0, END)
        email_input2.delete(0, END)
        password_input3.delete(0, END) 
        

# ---------------------------- UI SETUP ------------------------------- # 
window = Tk() 
window.title("Password manager")
window.minsize(width = 300, height = 300) 
window.config(padx= 40,pady= 40)

canvas = Canvas(width=240, height=240) 
photo = PhotoImage( file = "day 29/logo.png") 
canvas.create_image(120, 120, image = photo)
canvas.grid(column= 1, row= 0) 

# CREATING INPUTS
website_input1 = Entry(width= 58)
website_input1.grid(column= 1, row= 1, columnspan= 2)
website_input1.focus

email_input2 = Entry(width= 58)
email_input2.grid(column= 1, row= 2, columnspan= 2) 

password_input3 = Entry(width= 30)
password_input3.grid(column= 1, row= 3)  

# CREATING BUTTONS 
generate_password = Button(text= "Generate password", command= generate_password)
generate_password.grid(column= 2, row= 3) 

add_button = Button(text= "Add", width= 50, command= save)
add_button.grid(column= 1, row= 4, columnspan= 2)


# CREATING LABELS
web_label = Label(text= "Website:") 
web_label.grid(column= 0, row= 1)

mail_label = Label(text= "Email/ Username:") 
mail_label.grid(column= 0, row= 2)

password_label = Label(text= "Password:")
password_label.grid(column= 0, row= 3)

window.mainloop()
