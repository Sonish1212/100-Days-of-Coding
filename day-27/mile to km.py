FONT = ("Arial", 14)

from tkinter import *


def convert():
    value = int(mile.get())
    km = value * 1.609
    answer_label.config(text=km)


window = Tk()
window.title("Miles to Km Convertor")
window.config(padx=20, pady=20)

mile = Entry(width=15)
mile.grid(row=2, column=1)

mile_label = Label(text="Miles", font=FONT)
mile_label.grid(row=2, column=2)
mile_label.config(padx=4, pady=4)

equal_label = Label(text="is Equal to", font=FONT)
equal_label.grid(row=3, column=0)
equal_label.config(padx=4, pady=4)

answer_label = Label(text="0", font=FONT)
answer_label.grid(row=3, column=1)
answer_label.config(padx=4, pady=4)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=3, column=2)
km_label.config(padx=4, pady=4)

calc_button = Button(text="Calculate", font=FONT, command=convert)
calc_button.grid(row=5, column=1)
calc_button.config(padx=4, pady=4)

window.mainloop()
