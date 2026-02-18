from tkinter import * 
from datetime import date 

root = Tk() 
root.title("Widgets and stuff") 
root.geometry("300x250") # Slightly larger to fit content

# 1. Added quotes to all string values
lbl = Label(text="Hey there!", fg="black", bg="#11D9E8", height=1, width=30) 
name_lbl = Label(text="Full Name", bg="#00FFB7",fg="black") 
name_entry = Entry() 

def display(): 
    name = name_entry.get() 
    # Use f-strings or explicit concatenation for clarity
    message = f"Welcome to the Application!\nToday's date is: {date.today()}"
    greet = "Hello " + name + "\n"
    
    # Clear previous text if necessary (optional)
    text_box.delete('1.0', END)
    text_box.insert(END, greet) 
    text_box.insert(END, message) 

text_box = Text(height=3, width=30) 
# Added quotes to color values
btn = Button(text="Begin", command=display, height=1, bg="#00FF6A", fg="black") 

lbl.pack(pady=5) 
name_lbl.pack(pady=5) 
name_entry.pack(pady=5) 
btn.pack(pady=5) 
text_box.pack(pady=5) 

root.mainloop()
