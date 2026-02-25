from tkinter import *
window=Tk()
window.title("Event handler")
window.geometry("75x30")

def handle_keypress(event):
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("\nButton was pressed")
button=Button(text="Click Me!")
button.pack()
window.bind("<Button-1>",handle_click)
window.mainloop()