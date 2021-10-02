from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pandas.read_csv("data/words to know.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/Nepaliwords.csv")
    to_learn = df.to_dict(orient='records')
    current_card = {}
else:
    to_learn = df.to_dict(orient='records')
    current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas_card.itemconfig(card_title, text='Nepali', fill='black')
    canvas_card.itemconfig(card_word, text=current_card['Nepali'], fill='black')
    canvas_card.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, change_card)


def change_card():
    canvas_card.itemconfig(card_title, text='English', fill='white')
    canvas_card.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas_card.itemconfig(card_background, image=card_back)


def word_known():
    to_learn.remove(current_card)
    next_card()
    unknown_word = pandas.DataFrame(to_learn)
    unknown_word.to_csv('data/words to know.csv', index=False)


window = Tk()
window.title("Flash Cards")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, change_card)

canvas_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas_card.create_image(400, 263, image=card_front)
card_title = canvas_card.create_text(400, 150, text="Hi", fill='black', font=('Arial', 40, 'italic'))
card_word = canvas_card.create_text(400, 263, text="Salut", font=('Arial', 60, 'bold'))
canvas_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card.grid(row=0, column=0, columnspan=3)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=2)

card_right = PhotoImage(file="images/right.png")
known_button = Button(image=card_right, highlightthickness=0, command=word_known)
known_button.grid(row=1, column=0)

next_card()

window.mainloop()
