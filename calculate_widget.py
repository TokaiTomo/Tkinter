from tkinter import * 

c_w = Tk() 
c_w.title("Widgets and stuff") 
c_w.geometry("300x250")

lbl = Label(text="MULTIPLY YOUR NUMBERS", fg="black", bg="#ACDBDE", height=1, width=30) 
number_1 = Label(text="First Number", bg="#00FFB7",fg="black")
num_1 = Entry() 
number_2 = Label(text="Second Number", bg="#00FFB7",fg="black")
num_2 = Entry() 

def display():
    num1_str = num_1.get()
    num2_str = num_2.get()
    num_a,num_b=float(num1_str),float(num2_str)
    result = num_a * num_b
    answer="Your answer is: " + f"{result}"
    text_box.delete('1.0', END)
    text_box.insert(END, answer) 

text_box = Text(height=5, width=50)
start = Button(text="Multiply!", command=display, height=1, bg="#00FF6A", fg="black") 
lbl.pack(pady=5) 
number_1.pack(pady=5)
num_1.pack(pady=5)
number_2.pack(pady=5)
num_2.pack(pady=5)  
start.pack(pady=5) 
text_box.pack(pady=5)

c_w.mainloop()