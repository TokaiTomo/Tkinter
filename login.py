from tkinter import *
window=Tk()
window.title('Login Screen')
window.geometry('400x400')

frame=Frame(master=window,height=200, width=360, bg='#d0efff')

lbl1=Label(frame, text='Full Name', bg='#3895D3', fg='white', width=12)
lbl2=Label(frame, text='Email', bg='#3895D3', fg='white', width=12)
lbl3=Label(frame, text='Password', bg='#3895D3', fg='white', width=12)

sign = "*"
def change():
    if pass_entry.cget('show') == '':
        # Hide password
        pass_entry.config(show='*')
    else:
        # Show password
        pass_entry.config(show='')



def display():
    name=name_entry.get()
    greet="Hey "+name
    message="\nCongratulations for your new account!"
    textbox.insert(END,greet)
    textbox.insert(END,message)
textbox=Text(bg='#BEBEBE', fg='black')
btn=Button(text="Create Account", command=display, bg='red')
btn_2=Button(text="Show/Hide password", command=change, bg='blue')

name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame, show=sign)

frame.place(x=20,y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn_2.place(x=40, y=210)
btn.place(x=200, y=210)
textbox.place(y=250)
window.mainloop()