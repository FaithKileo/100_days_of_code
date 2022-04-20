# import tkinter 
# # we write as above when we want to use a specific class but when we want to use all of them we write

from tkinter import * 
# when we write it that way we wont have to tap into the class and again in the module,we juc go direct as normal.

window = Tk()

window.title("My first GUI program")
window.minsize(width = 500, height = 500)
# this leaves a bit of space to the x and y 
window.config(padx= 100, pady= 200)

my_label = Label( text = "I am a label", font= ("Arial", 24))
# my_label.pack() 
# grid is another way of placing something on a screen.
my_label.grid(column=0 , row= 0)

# when we want to change something eg a text. 
my_label["text"] = "New text" 
my_label.config(text= "New text")

# Button  
def button_clicked():
    print("I got clicked") 
    my_label.config(text= entry.get())
    
button = Button(text= "click me", command= button_clicked)
# button.pack() 
button.grid(column=1, row= 1)

new_button = Button(text = "New button")
new_button.grid(column=2 , row=0)

# entry 
entry = Entry(width= 20)
# entry.pack()
entry.grid(column=3, row= 2)
print(entry.get())


window.mainloop()