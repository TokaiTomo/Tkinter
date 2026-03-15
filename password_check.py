from tkinter import *
window=Tk()
window.title("Password Strength")
window.geometry("300x200")
def len_check():
    passcode=pass_entry.get()
    len_pass=len(passcode)
    if len_pass <= 5:
        result="weak"
    elif len_pass >=6 and len_pass<= 8:
        result="mid"
    elif len_pass >8 and len_pass<= 12:
        result="strong"
    elif len_pass > 12:
        result="very strong"
    lbl2.configure(text=result)
    return result
lbl1=Label(text="Your password", bg="#00FFB7",fg="black")
pass_entry=Entry()
button=Button(text="check", command=len_check, bg="#00FFB7",fg="black")
lbl2=Label(text=" ", fg="black")
lbl1.pack()
pass_entry.pack()
button.pack()
lbl2.pack()
window.mainloop()