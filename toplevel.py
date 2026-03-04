from tkinter import * 
window=Tk()
window.geometry("250x50")
window.title("main")

def topwin():
    top=Toplevel()
    top.geometry("180x50")
    top.title("toplevel window")
    l2=Label(top,text="this is the toplevel window")
    l2.pack()
    top.mainloop()

l=Label(text="This is the main window", bg="#0091FF")
btn=Button(text="Click here to open another window", command=topwin)

l.pack()
btn.pack()

window.mainloop()