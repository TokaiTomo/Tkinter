from tkinter import *
window=Tk()
window.title('meters to feet convert')
window.geometry('300x120')

lbl1=Label(window, text='Number in Meters', bg='#3895D3', fg='white')

def display():
    meter=entry.get()
    meter=float(meter)
    message=meter*3.28
    message=str(message)
    textbox.delete("1.0", END)
    textbox.insert(END,message)
    
textbox=Text(bg="#000000", fg='white')
btn=Button(window, text="Convert", command=display, bg='white')
entry=Entry()


lbl1.pack()
entry.pack()
btn.pack()
textbox.pack()
window.mainloop()