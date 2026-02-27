from tkinter import *
from datetime import *
c_w = Tk() 
c_w.title("Age calculator") 
c_w.geometry("300x350")
lbl = Label(text="Calculate your age", fg="black", bg="#ACDBDE", height=1, width=30) 
year_lbl = Label(text="Year of birth", bg="#00FFB7",fg="black")
year=Entry()
month_lbl=Label(text="Month of birth", bg="#00FFB7",fg="black")
month=Entry()
day_lbl=Label(text="Day of birth", bg="#00FFB7",fg="black")
day=Entry()


def display():
    yr = int(year.get())
    mt = int(month.get())
    dy = int(day.get())
    
    birth_date=date(yr,mt,dy)
    # Converting the string to a date object
    today=date.today()
    
    # Your original calculation method
    age = today.year - birth_date.year
    if (today.month, today.day)<(birth_date.month,birth_date.day):
        age-=1
    message=f"Your age is {age}."
    if birth_date>today:
        textbox.insert(END,"error")
    else:
        textbox.insert(END,message)
start=Button(text="Calculate age", command=display, height=1, bg="#00FF6A", fg="black")
textbox=Text(bg="#FFFFFF", fg='black')
lbl.pack(pady=5)
year_lbl.pack(pady=5)
year.pack(pady=5)
month_lbl.pack(pady=5)
month.pack(pady=5)
day_lbl.pack(pady=5)
day.pack(pady=5)
start.pack(pady=5)
textbox.pack(pady=5)
c_w.mainloop()