from tkinter import *
from tkinter import messagebox
box=Tk()
box.title("Pop up buttons")
box.geometry("75x300")

def alert():
    messagebox.showwarning("Alert","You pressed the button for alert")
def info():
    messagebox.showinfo("Info","You pressed the button for information")
def error():
    messagebox.showerror("Error","You pressed the button for error")
def ask():
    messagebox.askquestion("Ask","Did you push the button for asking a question?")
def ask_y_n():
    messagebox.askyesno("Ask","Did you push the button for asking a yes or no question?")
def ask_retry():
    messagebox.askretrycancel("Ask","You pressed the button for asking retry or cancel.")
def ask_ok():
    messagebox.askokcancel("Ask","You pressed the button to ask ok or cancel")
btn_1=Button(box, text="Alert",command=alert)
btn_2=Button(box, text="Info",command=info)
btn_3=Button(box, text="Error",command=error)
btn_4=Button(box, text="Ask",command=ask)
btn_5=Button(box, text="Y or N",command=ask_y_n)
btn_6=Button(box, text="Retry",command=ask_retry)
btn_7=Button(box, text="Ok",command=ask_ok)
btn_1.pack(pady=5)
btn_2.pack(pady=5)
btn_3.pack(pady=5)
btn_4.pack(pady=5)
btn_5.pack(pady=5)
btn_6.pack(pady=5)
btn_7.pack(pady=5)
box.mainloop()