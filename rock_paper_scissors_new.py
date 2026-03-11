import random
from tkinter import *
window=Tk()
window.geometry("400x250")
window.title("Rock Paper Scissors")
window.config(bg="blue")
choices=["rock","paper","scissors"]
def win_lose(user):
    computer=random.choice(choices)
    if computer == user: 
        result="Draw"
    elif (computer == "rock" and user == "paper") or \
        (computer == "paper" and user == "scissors")or \
        (computer == "scissors" and user == "rock"):
        result="Player Wins"
    else:
        result="Computer Wins"
    lbl_comp.config(text=f"Computer chose: \n{computer}")
    result_lbl.config(text=result)
button1=Button(text="Rock", command=lambda:win_lose("rock"), bg="blue", fg="blue", font=("Arial",17,"bold"))
button2=Button(text="Paper", command=lambda:win_lose("paper"), bg="blue", fg="blue", font=("Arial",17,"bold"))
button3=Button(text="Scissors", command=lambda:win_lose("scissors"), bg="blue", fg="blue", font=("Arial",17,"bold"))

button1.pack()
button2.pack()
button3.pack()
lbl_comp=Label(window, text=f"Computer chose:\n", bg="blue", font=("Arial", 20))
result_lbl=Label(window, text="", bg="blue", font=("Arial",20))
lbl_comp.pack()
result_lbl.pack()
window.mainloop()
