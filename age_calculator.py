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
    yr = str(year.get())
    mt = str(month.get())
    dy = str(day.get())
    dob_1 = yr + "-" + mt + "-" + dy
    
    # Converting the string to a date object
    birth_date = datetime.strptime(dob_1, "%Y-%m-%d").date()
    
    # Your original calculation method
    age = date.today() - birth_date
    if birth_date>date.today:
        textbox.insert(END,"error")
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
c_w.mainloop()