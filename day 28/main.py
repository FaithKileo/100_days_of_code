from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 0.5
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # if its the 8th rep:
        count_down(long_break_sec)
        time_label.config(text = "Break" , fg = RED)
        
    elif reps % 2 == 0:
        # if its the 2nd/4th/6th rep:
        count_down(short_break_sec)
        time_label.config(text = "Break" , fg = PINK) 
        
    else:
        # if its the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        time_label.config(text = "Work" , fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/ 60)
    count_sec = count % 60 
    
    if count_sec == 0:
        count_sec = "00" 
        
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- # 

window = Tk() 
window.title("Pomodoro app")
window.minsize(width = 300, height = 300)
window.config(padx= 50, pady= 50, bg= YELLOW)

canvas = Canvas(width= 200, height= 223, bg= YELLOW, highlightthickness= 0)
# highlightthickness, hides the boundary drawn box like around smthng and returns it plain 
photo = PhotoImage(file = "day 28/tomato.png")
canvas.create_image(100, 110, image= photo)
timer_text = canvas.create_text(102, 135, text = "00:00",fill = "black", font = (FONT_NAME, 40, "bold"))
canvas.grid(column= 1, row= 2)

time_label = Label(text= "Timer", fg = GREEN , bg = YELLOW, highlightthickness=0, font= (FONT_NAME, 30, "bold"))
time_label.grid(column= 1, row= 0) 

mark_label = Label(text= "@", font= (FONT_NAME, 15, "bold"))
mark_label.grid(column= 1, row= 4)

reset_button = Button(text= "Reset", font = (FONT_NAME, 10, "bold"))
reset_button.grid(column= 2, row= 3) 

start_button = Button(text= "Start", font = (FONT_NAME, 10, "bold"), command= start_timer)
start_button.grid(column= 0, row= 3) 

window.mainloop()