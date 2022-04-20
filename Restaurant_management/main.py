from tkinter import * 
from tkinter import filedialog,messagebox
import random
import time
import requests

# functions
def send():
    def send_msg():
        message = textarea.get(1.0, END)
        number = numberfield.get()
        auth = 'weBQKBrtZzLnD2ZUEnUYJIO40zZGnjgZm3BA1SAUd0qZ56gHm0k3X45DWR9c'
        url = 'https://www.fast2sms.com/dev/bulk'
        
        params = {
            'authorisation': auth,
            'message': number,
            'sender_id': 'FASTSMS',
            'route': 'p',
            'lanuage': 'english'    
        }
        response = requests.get(url, params = params)
        dic = response.json()
        result = dic.get('return')
        
        if result == True:
            messagebox.showinfo('Send successfully', 'Message sent was successfully')
            
        else:
            messagebox.showerror('Error', 'Something went wrong')
    
    root2 = Toplevel()
     
    root2.title("SEND BILL")
    root2.config(bg = 'red4')
    root2.minsize(width = 485, height =620 )
    
        # logoImage = PhotoImage(file = 'Restaurant_management\Screenshot_20220418-154736_Google.jpg')
        # label = Label(root2, image = logoImage)
        # label.pack()
    
    numberLabel = Label(root2, text= 'Mobile Number', font = ('arial', 18, 'bold underline'), bg = 'red4', fg = 'white')
    numberLabel.pack(pady = 5)
    
    numberfield = Entry(root2, font = ('helvetica', 22, 'bold'), bd = 3, width= 24)
    numberfield.pack(pady = 5)
    
    billLabel = Label(root2, text= 'Bill details', font = ('arial', 18, 'bold underline'), bg = 'red4', fg = 'white')
    billLabel.pack(pady = 5)
    
    textarea = Text(root2, font = ('arial', 12, 'bold'), bd = 3, width = 42, height = 14)
    textarea.pack(pady = 5)
    textarea.insert(END, 'Receipt Ref:\t\t' + billnumber +'\t\t' + date + '\n\n')
    
    textarea.insert(END, f"Cost of food\t\t\t{priceofFood}Rs\n")   
    textarea.insert(END, f"Cost of drinks\t\t\t{priceofDrinks}Rs\n")
    textarea.insert(END, f"Cost of cakes\t\t\t{priceofCakes}Rs\n")
    
    textarea.insert(END, f"Subtotal of Items\t\t\t{subtotalofItems}Rs\n")
    textarea.insert(END, f"Service tax\t\t\t{50}Rs\n")
    textarea.insert(END, f"Total cost\t\t\t{subtotalofItems + 50}Rs\n")
    
    
    sendbutton  = Button(root2, text = 'SEND', font = ('arial', 19, 'bold'), bg = 'white', fg = 'red4', bd=7, relief=GROOVE, command = send_msg)
    sendbutton.pack(pady = 5)
    
    root2.mainloop()

def save():
    url =  filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    
    bill_data = textReceipt.get(1.0, END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information', 'Your bill has been saved successfully.')

def receipt():
    global billnumber, date
   
    textReceipt.delete(1.0, END)
    x = random.randint(100, 10000)
    billnumber = 'BILL ' + str(x)
    date = time.strftime('%d/%m/%Y')
   
    textReceipt.insert(END, 'Receipt Ref: '+ billnumber + '\t \t' +date + '\n')
    textReceipt.insert(END,'****************************************************************************************************\n')
    textReceipt.insert(END, 'Items:\t\t Cost of items(Rs)\n')
    textReceipt.insert(END,'****************************************************************************************************\n')
    
    if e_roti.get() != '0':
        textReceipt.insert(END, f"Roti\t\t{int(e_roti.get())*10}\n\n")
    
    if e_daal.get() != '0':
        textReceipt.insert(END, f"Daal\t\t{int(e_daal.get())*60}\n\n") 
        
    if e_fish.get() != '0':
        textReceipt.insert(END, f"Fish\t\t{int(e_fish.get())*100}\n\n") 
        
    if e_sabji.get() != '0':
        textReceipt.insert(END, f"Sabji\t\t{int(e_sabji.get())*50}\n\n")
        
    if e_paneer.get() != '0':
        textReceipt.insert(END, f"Paneer\t\t{int(e_paneer.get())*100}\n\n")
        
    if e_kebab.get() != '0':
        textReceipt.insert(END, f"Kebab\t\t{int(e_kebab.get())*40}\n\n")
        
    if e_chawal.get() != '0':
        textReceipt.insert(END, f"Chawal\t\t{int(e_chawal.get())*30}\n\n")   
        
    if e_chicken.get() != '0':
        textReceipt.insert(END, f"Chicken\t\t{int(e_chicken.get())*120}\n\n") 
    
    if e_mutton.get() != '0':
        textReceipt.insert(END, f"Mutton\t\t{int(e_mutton.get())*10}\n\n") 
        
    if e_lassi.get() != '0':
        textReceipt.insert(END, f"Lassi\t\t{int(e_lassi.get())*50}\n\n")     
        
    if e_coffee.get() != '0':
        textReceipt.insert(END, f"Coffee\t\t{int(e_coffee.get())*40}\n\n")   
        
    if e_faluda.get() != '0':
        textReceipt.insert(END, f"Faluda\t\t{int(e_faluda.get())*80}\n\n")    
        
    if e_shikanji.get() != '0':
        textReceipt.insert(END, f"Shikanji\t\t{int(e_shikanji.get())*30}\n\n")    
        
    if e_jaljeera.get() != '0':
        textReceipt.insert(END, f"Jaljeera\t\t{int(e_jaljeera.get())*40}\n\n")  
        
    if e_roohfza.get() != '0':
        textReceipt.insert(END, f"Roohfza\t\t{int(e_roohfza.get())*60}\n\n")      
        
    if e_masalatea.get() != '0':
        textReceipt.insert(END, f"Masalatea\t\t{int(e_masalatea.get())*20}\n\n")    
        
    if e_badammilk.get() != '0':
        textReceipt.insert(END, f"Badammilk\t\t{int(e_badammilk.get())*50}\n\n")   
        
    if e_colddrinks.get() != '0':
        textReceipt.insert(END, f"Colddrinks\t\t{int(e_colddrinks.get())*80}\n\n")   
        
    if e_oreo.get() != '0':
        textReceipt.insert(END, f"Oreo\t\t{int(e_oreo.get())*400}\n\n")   
        
    if e_apple.get() != '0':
        textReceipt.insert(END, f"Apple\t\t{int(e_apple.get())*300}\n\n")    
        
    if e_kitkatcake.get() != '0':
        textReceipt.insert(END, f"Kitkatcake\t\t{int(e_kitkatcake.get())*500}\n\n")   
        
    if e_vanilla.get() != '0':
        textReceipt.insert(END, f"Vanilla\t\t{int(e_vanilla.get())*550}\n\n")    
        
    if e_banana.get() != '0':
        textReceipt.insert(END, f"Banana\t\t{int(e_banana.get())*450}\n\n")   
        
    if e_brownie.get() != '0':
        textReceipt.insert(END, f"Brownie\t\t{int(e_brownie.get())*800}\n\n")     
        
    if e_pineapple.get() != '0':
        textReceipt.insert(END, f"Pineapple\t\t{int(e_pineapple.get())*620}\n\n")   
        
    if e_chocolate.get() != '0':
        textReceipt.insert(END, f"Chocolate\t\t{int(e_chocolate.get())*700}\n\n")    
        
    if e_blackforest.get() != '0':
        textReceipt.insert(END, f"Blackforest\t\t{int(e_blackforest.get())*550}\n\n")   
        
    textReceipt.insert(END,'****************************************************************************************************\n')
    
    textReceipt.insert(END, f"Cost of food\t\t\t{priceofFood}Rs\n\n")   
    textReceipt.insert(END, f"Cost of drinks\t\t\t{priceofDrinks}Rs\n\n")
    textReceipt.insert(END, f"Cost of cakes\t\t\t{priceofCakes}Rs\n\n")
    
    textReceipt.insert(END,'****************************************************************************************************\n')
    
    textReceipt.insert(END, f"Subtotal of Items\t\t\t{subtotalofItems}Rs\n\n")
    textReceipt.insert(END, f"Service tax\t\t\t{50}Rs\n\n")
    textReceipt.insert(END, f"Total cost\t\t\t{subtotalofItems + 50}Rs\n\n")
    
def totalcost():
    global priceofFood,priceofCakes,priceofDrinks,subtotalofItems
    
    item1 = int(e_roti.get())
    item2 = int(e_daal.get())
    item3 = int(e_fish.get())
    item4 = int(e_sabji.get()) 
    item5 = int(e_kebab.get()) 
    item6 = int(e_chawal.get()) 
    item7 = int(e_mutton.get()) 
    item8 = int(e_paneer.get())
    item9 = int(e_chicken.get()) 
    
    item10 = int(e_lassi.get())
    item11 = int(e_coffee.get()) 
    item12 = int(e_faluda.get()) 
    item13 = int(e_shikanji.get()) 
    item14 = int(e_jaljeera.get())
    item15 = int(e_roohfza.get())
    item16 = int(e_masalatea.get()) 
    item17 = int(e_badammilk.get()) 
    item18 = int(e_colddrinks.get()) 

    item19 = int(e_oreo.get())
    item20 = int(e_apple.get()) 
    item21 = int(e_kitkatcake.get()) 
    item22 = int(e_vanilla.get()) 
    item23 = int(e_banana.get()) 
    item24 = int(e_brownie.get()) 
    item25 = int(e_pineapple.get())
    item26 = int(e_chocolate.get()) 
    item27 = int(e_blackforest.get()) 
    
    priceofFood = (item1*10) + (item2*60) + (item3*100) + (item4*50) + (item5*40) \
                  + (item6*30) + (item7*120) + (item8*100) + (item9*120)
                  
    priceofDrinks = (item10*50) + (item11*40) + (item12*80) + (item13*30) + (item14*40) \
                  + (item15*60) + (item16*20) + (item17*50) + (item18*80)
    
    priceofCakes = (item19*400) + (item20*300) + (item21*500) + (item22*550) + (item23*450) \
                  + (item24*800) + (item25*620) + (item26*700) + (item27*550)
    
    costoffoodvar.set(str(priceofFood) + 'Rs') 
    costofdrinksvar.set(str(priceofDrinks) + 'Rs') 
    costofcakesvar.set(str(priceofCakes) + 'Rs') 
    
    subtotalofItems = priceofFood + priceofDrinks + priceofCakes 
    labelsubtotalvar.set(str(subtotalofItems) + 'Rs' )
    
    textservicetaxvar.set('50 Rs')
    
    totalcost = subtotalofItems + 50 
    labeltotalcostvar.set(str(totalcost) + 'Rs') 
    

def rooti():
    if var1.get() == 1:
        textroti.config(state= NORMAL)
        textroti.focus()
        textroti.delete(0, END)
    else:
        textroti.config(state = DISABLED)
        e_roti.set('0')

def dal():
    if var2.get() == 1:
        textdaal.config(state= NORMAL)
        textdaal.focus()
        textdaal.delete(0, END)
    else:
        textdaal.config(state = DISABLED)
        e_daal.set('0')
        
def fishy():
    if var3.get() == 1:
        textfish.config(state= NORMAL)
        textfish.focus()
        textfish.delete(0, END)
    else:
        textfish.config(state = DISABLED)
        e_fish.set('0')
        
def sabj():
    if var4.get() == 1:
        textsabji.config(state= NORMAL)
        textsabji.focus()
        textsabji.delete(0, END)
    else:
        textsabji.config(state = DISABLED)
        e_sabji.set('0')
        
def kebabu():
    if var5.get() == 1:
        textkebab.config(state= NORMAL)
        textkebab.focus()
        textkebab.delete(0, END)
    else:
        textkebab.config(state = DISABLED)
        e_kebab.set('0')       
        
def chawali():
    if var6.get() == 1:
        textchawal.config(state= NORMAL)
        textchawal.focus()
        textchawal.delete(0, END)
    else:
        textchawal.config(state = DISABLED)
        e_chawal.set('0')   
        
def mutto():
    if var7.get() == 1:
        textmutton.config(state= NORMAL)
        textmutton.focus()
        textmutton.delete(0, END)
    else:
        textmutton.config(state = DISABLED)
        e_mutton.set('0')       
        
def pane():
    if var8.get() == 1:
        textpaneer.config(state= NORMAL)
        textpaneer.focus()
        textpaneer.delete(0, END)
    else:
        textpaneer.config(state = DISABLED)
        e_paneer.set('0') 
        
def chick():
    if var9.get() == 1:
        textchicken.config(state= NORMAL)
        textchicken.focus()
        textchicken.delete(0, END)
    else:
        textchicken.config(state = DISABLED)
        e_chicken.set('0')    

def lassi():
    if var10.get() == 1:
        textlassi.config(state= NORMAL)
        textlassi.focus()
        textlassi.delete(0, END)
    else:
        textlassi.config(state = DISABLED)
        e_lassi.set('0')       
        
def coffee():
    if var11.get() == 1:
        textcoffee.config(state= NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    else:
        textcoffee.config(state = DISABLED)
        e_coffee.set('0')    

def faluda():
    if var12.get() == 1:
        textfaluda.config(state= NORMAL)
        textfaluda.focus()
        textfaluda.delete(0, END)
    else:
        textfaluda.config(state = DISABLED)
        e_faluda.set('0')   
             
def shikanji():
    if var13.get() == 1:
        textshikanji.config(state= NORMAL)
        textshikanji.focus()
        textshikanji.delete(0, END)
    else:
        textshikanji.config(state = DISABLED)
        e_shikanji.set('0')   

def jaljeera():
    if var14.get() == 1:
        textjaljeera.config(state= NORMAL)
        textjaljeera.focus()
        textjaljeera.delete(0, END)
    else:
        textjaljeera.config(state = DISABLED)
        e_jaljeera.set('0')   
        
def roohafza():
    if var15.get() == 1:
        textroohfza.config(state= NORMAL)
        textroohfza.focus()
        textroohfza.delete(0, END)
    else:
        textroohafza.config(state = DISABLED)
        e_roohfza.set('0')   
        
def masalatea():
    if var16.get() == 1:
        textmasalatea.config(state= NORMAL)
        textmasalatea.focus()
        textmasalatea.delete(0, END)
    else:
        textmasalatea.config(state = DISABLED)
        e_masalatea.set('0')   
     
def badammilk():
    if var17.get() == 1:
        textbadammilk.config(state= NORMAL)
        textbadammilk.focus()
        textbadammilk.delete(0, END)
    else:
        textbadammilk.config(state = DISABLED)
        e_badammilk.set('0')      
        
def colddrinks():
    if var18.get() == 1:
        textcolddrinks.config(state= NORMAL)
        textcolddrinks.focus()
        textcolddrinks.delete(0, END)
    else:
        textcolddrinks.config(state = DISABLED)
        e_colddrinks.set('0')   
        
def oreo():
    if var19.get() == 1:
        textoreo.config(state= NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
    else:
        textoreo.config(state = DISABLED)
        e_oreo.set('0')           
        
def apple():
    if var20.get() == 1:
        textapple.config(state= NORMAL)
        textapple.focus()
        textapple.delete(0, END)
    else:
        textapple.config(state = DISABLED)
        e_apple.set('0')   

def kitkat():
    if var21.get() == 1:
        textkitkatcake.config(state= NORMAL)
        textkitkatcake.focus()
        textkitkatcake.delete(0, END)
    else:
        textkitkat.config(state = DISABLED)
        e_kitkat.set('0')   
      
def vanilla():
    if var22.get() == 1:
        textvanilla.config(state= NORMAL)
        textvanilla.focus()
        textvanilla.delete(0, END)
    else:
        textvanilla.config(state = DISABLED)
        e_vanilla.set('0')   

def banana():
    if var23.get() == 1:
        textbanana.config(state= NORMAL)
        textbanana.focus()
        textbanana.delete(0, END)
    else:
        textbanana.config(state = DISABLED)
        e_banana.set('0')   

def brownie():
    if var24.get() == 1:
        textbrownie.config(state= NORMAL)
        textbrownie.focus()
        textbrownie.delete(0, END)
    else:
        textbrownie.config(state = DISABLED)
        e_brownie.set('0')   
 
def pineapple():
    if var25.get() == 1:
        textpineapple.config(state= NORMAL)
        textpineapple.focus()
        textpineapple.delete(0, END)
    else:
        textpineapple.config(state = DISABLED)
        e_pineapple.set('0')    

def chocolate():
    if var26.get() == 1:
        textchocolate.config(state= NORMAL)
        textchocolate.focus()
        textchocolate.delete(0, END)
    else:
        textchocolate.config(state = DISABLED)
        e_chocolate.set('0')   
      
def blackforest():
    if var27.get() == 1:
        textblackforest.config(state= NORMAL)
        textblackforest.focus()
        textblackforest.delete(0, END)
    else:
        textblackforest.config(state = DISABLED)
        e_blackforest.set('0')   
            
      
window = Tk() 

window.minsize(width = 1270, height = 690)
window.title("Restaurant management system created by Faith Kileo.") 
window.config(bg= "firebrick4")

topFrame = Frame(window, bd=10, relief = RIDGE, bg= 'firebrick4') 
# bd means boder, relief means style of the border.
topFrame.pack(side= TOP) 

labeltitle = Label(topFrame, text= 'Restaurant Management System', font= ('arial', 30, 'bold'),
                   fg = 'Yellow', bg ='red4', width= 56 )
labeltitle.grid(column=0, row= 0)

# frames
menuframe = Frame(window, bd = 10, relief= RIDGE, bg= 'firebrick4')
menuframe.pack(side= LEFT) 

costframe = Frame(menuframe, bd= 4, relief= RIDGE, bg= 'firebrick4', pady=30)
costframe.pack(side= BOTTOM)

foodframe = LabelFrame(menuframe, text= 'Food', font= ('arial', 19, 'bold'), bd=10, relief= RIDGE, fg= 'red4')
foodframe.pack(side= LEFT) 

drinksframe = LabelFrame(menuframe, text= 'Drinks', font= ('arial', 19, 'bold'), bd=10, relief= RIDGE, fg= 'red4')
drinksframe.pack(side= LEFT) 

cakesframe = LabelFrame(menuframe, text= 'Cakes', font= ('arial', 19, 'bold'), bd=10, relief= RIDGE, fg= 'red4')
cakesframe.pack(side= LEFT)

rightframe = Frame(window, bd=15, relief= RIDGE, bg= 'red4')
rightframe.pack(side= RIGHT) 

calculatorframe = Frame(rightframe, bd = 1, relief= RIDGE, pady=12, bg='red4')
calculatorframe.pack(side= TOP) 

receiptframe = Frame(rightframe, bd = 4, relief= RIDGE, bg='red4')
receiptframe.pack(side= TOP)

buttonframe = Frame(rightframe, bd = 3, relief= RIDGE, bg='red4')
buttonframe.pack(side= TOP) 

# variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24= IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
# foodvariables

e_roti = StringVar()
e_daal = StringVar()
e_fish = StringVar()
e_sabji = StringVar()
e_kebab = StringVar()
e_chawal = StringVar()
e_mutton = StringVar()
e_paneer = StringVar()
e_chicken = StringVar()

# drinksvariables

e_lassi = StringVar()
e_faluda = StringVar() 
e_coffee = StringVar() 
e_shikanji = StringVar()
e_jaljeera = StringVar() 
e_roohfza = StringVar() 
e_masalatea = StringVar() 
e_badammilk = StringVar() 
e_colddrinks = StringVar() 

# cakes variables 
e_oreo = StringVar() 
e_apple = StringVar() 
e_kitkatcake = StringVar() 
e_vanilla = StringVar() 
e_banana = StringVar() 
e_brownie = StringVar() 
e_pineapple = StringVar() 
e_chocolate = StringVar()
e_blackforest = StringVar()  

# setting zero in every place
e_roti.set('0')
e_daal.set('0')
e_fish.set('0')
e_sabji.set('0')
e_kebab.set('0')
e_chawal.set('0')
e_mutton.set('0')
e_paneer.set('0')
e_chicken.set('0') 

e_lassi.set('0')
e_faluda.set('0') 
e_coffee.set('0') 
e_shikanji.set('0')
e_jaljeera.set('0') 
e_roohfza.set('0') 
e_masalatea.set('0') 
e_badammilk.set('0') 
e_colddrinks.set('0')  

e_oreo.set('0') 
e_apple.set('0') 
e_kitkatcake.set('0') 
e_vanilla.set('0') 
e_banana.set('0') 
e_brownie.set('0') 
e_pineapple.set('0') 
e_chocolate.set('0')
e_blackforest.set('0')  

# costlabels and entry fields variables
costoffoodvar = StringVar() 
costofdrinksvar = StringVar() 
costofcakesvar = StringVar() 
labelsubtotalvar = StringVar() 
textservicetaxvar = StringVar() 
labeltotalcostvar = StringVar() 

# FOOD 

roti = Checkbutton(foodframe, text = 'Roti', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var1, command= rooti)
roti.grid(row=0, column=0, sticky= W)

daal = Checkbutton(foodframe, text = 'Daal', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var2, command= dal)
daal.grid(row=1, column=0, sticky= W)

fish = Checkbutton(foodframe, text = 'Fish', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var3, command=fishy)
fish.grid(row=2, column=0, sticky= W)

sabji = Checkbutton(foodframe, text = 'Sabji', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var4, command= sabj)
sabji.grid(row=3, column=0, sticky= W) 

kebab = Checkbutton(foodframe, text = 'Kebab', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var5, command= kebabu)
kebab.grid(row=4, column=0, sticky= W)

chawal = Checkbutton(foodframe, text = 'Chawal', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var6, command= chawali)
chawal.grid(row=5, column=0, sticky= W) 

mutton = Checkbutton(foodframe, text = 'Mutton', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var7, command= mutto)
mutton.grid(row=6, column=0, sticky= W) 

paneer = Checkbutton(foodframe, text = 'Paneer', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var8, command= pane)
paneer.grid(row=7, column=0, sticky= W) 

chicken = Checkbutton(foodframe, text = 'Chicken', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var9, command=chick)
chicken.grid(row=8, column=0, sticky= W)

# empty entries for food items 

textroti = Entry(foodframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_roti)
textroti.grid(row= 0, column=1)

textdaal = Entry(foodframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_daal)
textdaal.grid(row= 1, column=1)

textfish = Entry(foodframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_fish)
textfish.grid(row= 2, column=1)

textsabji = Entry(foodframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_sabji)
textsabji.grid(row= 3, column=1)

textkebab = Entry(foodframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_kebab)
textkebab.grid(row= 4, column=1)

textchawal = Entry(foodframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_chawal)
textchawal.grid(row= 5, column=1)

textmutton = Entry(foodframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_mutton)
textmutton.grid(row= 6, column=1)

textpaneer = Entry(foodframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_paneer)
textpaneer.grid(row= 7, column=1)

textchicken = Entry(foodframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_chicken)
textchicken.grid(row= 8, column=1) 

# Drinks 
lassi = Checkbutton(drinksframe, text = 'Lassi', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var10, command= lassi)
lassi.grid(row=0, column=0, sticky= W)

coffee = Checkbutton(drinksframe, text = 'Coffee', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var11, command = coffee)
coffee.grid(row=1, column=0, sticky= W)

faluda = Checkbutton(drinksframe, text = 'Faluda', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var12, command = faluda)
faluda.grid(row=2, column=0, sticky= W)

shikanji = Checkbutton(drinksframe, text = 'Shikanji', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var13, command = shikanji)
shikanji.grid(row=3, column=0, sticky= W)

jaljeera = Checkbutton(drinksframe, text = 'Jaljeera', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var14, command= jaljeera)
jaljeera.grid(row=4, column=0, sticky= W)

roohfza = Checkbutton(drinksframe, text = 'Roohfza', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var15, command= roohafza)
roohfza.grid(row=5, column=0, sticky= W)

masalatea = Checkbutton(drinksframe, text = 'Masalatea', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var16, command = masalatea)
masalatea.grid(row=6, column=0, sticky= W)

badammilk= Checkbutton(drinksframe, text = 'Badammilk', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var17, command = badammilk)
badammilk.grid(row=7, column=0, sticky= W)

colddrinks = Checkbutton(drinksframe, text = 'Colddrinks', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var18, command = colddrinks)
colddrinks.grid(row=8, column=0, sticky= W)

# empty entries for drinks items 

textlassi = Entry(drinksframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_lassi)
textlassi.grid(row= 0, column=1)

textcoffee = Entry(drinksframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_coffee)
textcoffee.grid(row= 1, column=1)

textfaluda = Entry(drinksframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_faluda)
textfaluda.grid(row= 2, column=1)

textshikanji = Entry(drinksframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_shikanji)
textshikanji.grid(row= 3, column=1)

textjaljeera = Entry(drinksframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_jaljeera)
textjaljeera.grid(row= 4, column=1)

textroohfza = Entry(drinksframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_roohfza)
textroohfza.grid(row= 5, column=1)

textmasalatea = Entry(drinksframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_masalatea)
textmasalatea.grid(row= 6, column=1)

textbadammilk = Entry(drinksframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_badammilk)
textbadammilk.grid(row= 7, column=1)

textcolddrinks = Entry(drinksframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_colddrinks)
textcolddrinks.grid(row= 8, column=1) 

# cakes

oreo = Checkbutton(cakesframe, text = 'Oreo', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var19, command= oreo)
oreo.grid(row=0, column=0, sticky= W)

apple = Checkbutton(cakesframe, text = 'Apple', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var20, command = apple)
apple.grid(row=1, column=0, sticky= W)

kitkatcake = Checkbutton(cakesframe, text = 'Kitkatcake', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var21, command = kitkat)
kitkatcake.grid(row=2, column=0, sticky= W)

vanilla = Checkbutton(cakesframe, text = 'Vanilla', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var22, command = vanilla)
vanilla.grid(row=3, column=0, sticky= W)

banana = Checkbutton(cakesframe, text = 'Banana', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var23, command = banana)
banana.grid(row=4, column=0, sticky= W)

brownie = Checkbutton(cakesframe, text = 'Brownie', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var24, command = brownie)
brownie.grid(row=5, column=0, sticky= W)

pineapple = Checkbutton(cakesframe, text = 'Pineapple', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var25, command = pineapple)
pineapple.grid(row=6, column=0, sticky= W)

chocolate= Checkbutton(cakesframe, text = 'Chocolate', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var26, command = chocolate)
chocolate.grid(row=7, column=0, sticky= W)

blackforest = Checkbutton(cakesframe, text = 'Blackforest', font= ('arial', 18, 'bold'),
                   onvalue=1, offvalue=0, variable= var27, command = blackforest)
blackforest.grid(row=8, column=0, sticky= W)

# empty entries for cakes 

textoreo = Entry(cakesframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_oreo)
textoreo.grid(row= 0, column=1)

textapple = Entry(cakesframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_apple)
textapple.grid(row= 1, column=1)

textkitkatcake = Entry(cakesframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_kitkatcake)
textkitkatcake.grid(row= 2, column=1)

textvanilla = Entry(cakesframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_vanilla)
textvanilla.grid(row= 3, column=1)

textbanana = Entry(cakesframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_banana)
textbanana.grid(row= 4, column=1)

textbrownie = Entry(cakesframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_brownie)
textbrownie.grid(row= 5, column=1)

textpineapple = Entry(cakesframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_pineapple)
textpineapple.grid(row= 6, column=1)

textchocolate = Entry(cakesframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_chocolate)
textchocolate.grid(row= 7, column=1)

textblackforest = Entry(cakesframe, font=('arial', 10, 'bold'), bd= 7 , width=6, state= DISABLED, textvariable= e_blackforest)
textblackforest.grid(row= 8, column=1)  

# costlabels and entry fields 

costoffood = Label(costframe, text='Cost of Food', font = ('arial', 16, 'bold'), bg= 'firebrick4', fg= 'white')
costoffood.grid(column=0, row=0) 

textcostoffood = Entry(costframe, font=('arial', 16, 'bold'), bd = 6, width=14, state= 'readonly', textvariable=costoffoodvar)
textcostoffood.grid(column=1 , row= 0, padx= 12)

costofdrinks = Label(costframe, text='Cost of drinks', font = ('arial', 16, 'bold'), bg= 'firebrick4', fg= 'white')
costofdrinks.grid(column=0, row=1) 

textcostofdrinks = Entry(costframe, font=('arial', 16, 'bold'), bd = 6, width=14, state= 'readonly', textvariable=costofdrinksvar)
textcostofdrinks.grid(column=1 , row= 1, padx= 12)

costofcakes = Label(costframe, text='Cost of cakes', font = ('arial', 16, 'bold'), bg= 'firebrick4', fg= 'white')
costofcakes.grid(column=0, row=2) 

textcostofcakes = Entry(costframe, font=('arial', 16, 'bold'), bd = 6, width=14, state= 'readonly', textvariable=costofcakesvar)
textcostofcakes.grid(column=1 , row= 2, padx= 12) 

labelsubtotal = Label(costframe, text='Sub total', font = ('arial', 16, 'bold'), bg= 'firebrick4', fg= 'white')
labelsubtotal.grid(column=2, row=0) 

textsubtotal = Entry(costframe, font=('arial', 16, 'bold'), bd = 6, width=14, state= 'readonly', textvariable=labelsubtotalvar)
textsubtotal.grid(column=3 , row= 0, padx= 12) 

labelservicetax = Label(costframe, text='Service tax', font = ('arial', 16, 'bold'), bg= 'firebrick4', fg= 'white')
labelservicetax.grid(column=2, row=1) 

textservicetax = Entry(costframe, font=('arial', 16, 'bold'), bd = 6, width=14, state= 'readonly', textvariable=textservicetaxvar)
textservicetax.grid(column=3 , row= 1, padx= 12) 

labeltotalcost = Label(costframe, text='Total cost', font = ('arial', 16, 'bold'), bg= 'firebrick4', fg= 'white')
labeltotalcost.grid(column=2, row=2) 

texttotalcost = Entry(costframe, font=('arial', 16, 'bold'), bd = 6, width=14, state= 'readonly', textvariable=labeltotalcostvar)
texttotalcost.grid(column=3 , row= 2, padx= 12) 

# Buttons 
buttontotal = Button(buttonframe, text= 'Total', font=('arial', 14, 'bold'),fg = 'white', bg= 'red4', bd=3, padx=25, command=totalcost)
buttontotal.grid(column=0, row= 0)

buttonreceipt = Button(buttonframe, text= 'Receipt', font=('arial', 14, 'bold'), fg = 'white', bg= 'red4', bd=3, padx=25, command= receipt)
buttonreceipt.grid(column=1, row= 0)

buttonsave = Button(buttonframe, text= 'Save', font=('arial', 14, 'bold'), fg = 'white', bg= 'red4', bd=3, padx=26, command = save)
buttonsave.grid(column=2, row= 0)

buttonsend = Button(buttonframe, text= 'Send', font=('arial', 14, 'bold'), fg = 'white', bg= 'red4', bd=3, padx=26, command = send)
buttonsend.grid(column=3, row= 0)

buttonreset = Button(buttonframe, text= 'Reset', font=('arial', 14, 'bold'), fg = 'white', bg= 'red4', bd=3, padx=26)
buttonreset.grid(column=4, row= 0)

# text area for receipt 
textReceipt = Text(receiptframe, font=('arial', 12, 'bold'), bd=3, width=67, height=14) 
textReceipt.grid(column= 0, row= 1)

# calculator field
operator = ''

def buttonClick(numbers):
    global operator
    operator += numbers
    calculatorfield.delete(0, END)
    calculatorfield.insert(END, operator) 
    
def clear():
    global operator
    operator = ''
    calculatorfield.delete(0, END)

def answer():
    global operator  
    result = str(eval(operator))
    calculatorfield.delete(0, END)
    calculatorfield.insert(0, result)
    operator = ''

calculatorfield = Entry(calculatorframe, font=('arial', 16, 'bold'), width=51, bd=4)
calculatorfield.grid(column = 0, row = 0, columnspan=4)

button7 = Button(calculatorframe, text='7', font=('arial', 16, 'bold'), bg='red4', fg='yellow',
                bd=6, width=10, command =lambda:buttonClick('7'))
button7.grid(column=0, row=1)

button8 = Button(calculatorframe, text='8', font=('arial', 16, 'bold'), bg='red4', fg='yellow',
                bd=6, width=11, command =lambda:buttonClick('8'))
button8.grid(column=1, row=1)

button9 = Button(calculatorframe, text='9', font=('arial', 16, 'bold'), bg='red4', fg='yellow',
                bd=6, width=11, command =lambda:buttonClick('9'))
button9.grid(column=2, row=1)

buttonplus = Button(calculatorframe, text='+', font=('arial', 16, 'bold'), bg='red4', fg='yellow',
                bd=6, width=10, command =lambda:buttonClick('+'))
buttonplus.grid(column=3, row=1)

button4 = Button(calculatorframe, text='4', font=('arial', 16, 'bold'), bg='red4', fg='yellow',
                bd=6, width=10, command =lambda:buttonClick('4'))
button4.grid(column=0, row=2)

button5 = Button(calculatorframe, text='5', font=('arial', 16, 'bold'), bg='white', fg='red4',
                bd=6, width=11, command =lambda:buttonClick('5'))
button5.grid(column=1, row=2)

button6 = Button(calculatorframe, text='6', font=('arial', 16, 'bold'), bg='white', fg='red4',
                bd=6, width=11, command =lambda:buttonClick('6'))
button6.grid(column=2, row=2)

buttonminus = Button(calculatorframe, text='-', font=('arial', 16, 'bold'), bg='red4', fg='yellow',
                bd=6, width=10, command =lambda:buttonClick('-'))
buttonminus.grid(column=3, row=2)

button1 = Button(calculatorframe, text='1', font=('arial', 16, 'bold'), bg='red4', fg='yellow',
                bd=6, width=10, command =lambda:buttonClick('1'))
button1.grid(column=0, row=3)

button2 = Button(calculatorframe, text='2', font=('arial', 16, 'bold'), bg='white', fg='red4',
                bd=6, width=11, command =lambda:buttonClick('2'))
button2.grid(column=1, row=3)

button3 = Button(calculatorframe, text='3', font=('arial', 16, 'bold'), bg='white', fg='red4',
                bd=6, width=11, command =lambda:buttonClick('3'))
button3.grid(column=2, row=3)

buttontimes = Button(calculatorframe, text='*', font=('arial', 16, 'bold'), bg='red4', fg='yellow',
                bd=6, width=10, command =lambda:buttonClick('*'))
buttontimes.grid(column=3, row=3)

buttonanswer = Button(calculatorframe, text='Ans', font=('arial', 16, 'bold'), bg='red4',
                fg='yellow', bd=6, width=10, command=answer)
buttonanswer.grid(column=0, row=4)

buttonclear = Button(calculatorframe, text='Clear', font=('arial', 16, 'bold'), bg='red4',
                fg='yellow', bd=6, width=11, command= clear)
buttonclear.grid(column=1, row=4) 

button0 = Button(calculatorframe, text='0', font=('arial', 16, 'bold'), bg='red4', fg='yellow',
                bd=6, width=11, command =lambda:buttonClick('0'))
button0.grid(column=2, row=4)

buttondivide = Button(calculatorframe, text='/', font=('arial', 16, 'bold'), bg='red4', fg='yellow',
                bd=6, width=10, command =lambda:buttonClick('/'))
buttondivide.grid(column=3, row=4)

window.mainloop()