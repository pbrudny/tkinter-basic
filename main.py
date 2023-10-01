
from tkinter import *

main = Tk()

def button_clicked():
    text = Label(main, text="This button has been clicked")
    text.pack()

button_one = Button(main, text="click me", fg="gold", highlightbackground="black", command=button_clicked)
button_one.pack()

button_two = Button(main, text="click me", fg="gold", highlightbackground="white", command=button_clicked)
button_two.pack(padx=50, pady=50)

main.mainloop()