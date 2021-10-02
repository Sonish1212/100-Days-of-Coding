from tkinter import *


def button_click():
    value = input.get()
    my_label.config(text=value)


window = Tk()
window.geometry("500x500")
window.config(padx=20, pady=20)

my_label = Label(text="Print here", font=("century", 24, 'bold'))
my_label.grid(row=0, column=0)


my_button = Button(text="Click Here", command=button_click)
my_button.grid(row=1, column=1)

input = Entry(width=10)
input.grid(row=2, column=3)

next_button = Button(text="Another Button")
next_button.grid(row=0, column=2)

window.mainloop()
