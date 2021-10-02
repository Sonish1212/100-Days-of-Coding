from tkinter import *
import pandas
import random
from timeit import default_timer as timer

BACKGROUND_COLOR = "#B1DDC6"
df = pandas.read_csv("data/sentences.csv")
to_learn = df.to_dict(orient='records')
current_card = {}


def next_sentence():
    global current_card
    current_card = random.choice(to_learn)
    canvas_card.itemconfig(card_title, text='Typing Test', fill='Red')
    canvas_card.itemconfig(card_word, text=current_card['sentences'], fill='black')
    canvas_card.itemconfig(card_background, image=card_front)
    filename.delete("1.0", "end")


def check_time():
    j = error = 0
    answer = filename.get('1.0', 'end-1c')
    end = timer()
    time_taken = end - start
    if len(current_card['sentences']) >= len(answer):
        error = len(current_card['sentences']) - len(answer)
        for i in answer:
            if i == current_card['sentences']:
                pass
            else:
                error += 1
            j += 1
    elif len(current_card['sentences']) <= len(answer):
        error = len(current_card['sentences']) - len(answer)
        for i in answer:
            if i == current_card['sentences']:
                pass
            else:
                error += 1
            j += 1
    wpm = len(answer)/5
    wpm = error - wpm
    wpm = int(wpm/(time_taken/60))
    new_window = Toplevel(window)
    new_window.config(bg='black', padx=100, pady=50)
    new_window.title("Result Window")
    heading = Label(new_window, text="Your Typing Speed is displayed Below", font=('Century Gothic', 30, 'bold'), bg='#000', fg='#f00')
    heading.grid(row=0, column=0, columnspan=3)
    time_label = Label(new_window, text="Time", font=('Century Gothic', 20, 'bold'), bg='#000', fg='#f00')
    time_label.grid(row=1, column=0, ipady=80)
    time_answer = Label(new_window, text=wpm, font=('Century Gothic', 14, 'bold'), bg='#000', fg='#f00')
    time_answer.grid(row=2, column=0)

    review_label = Label(new_window, text="Review", font=('Century Gothic', 20, 'bold'), bg='#000', fg='#f00')
    review_label.grid(row=1, column=2, ipady=80)
    review_answer = Label(new_window, text="You can always do better remember that", font=('Century Gothic', 14, 'bold'), bg='#000', fg='#f00')
    review_answer.grid(row=2, column=2)




# def open_new_window():
#     # Toplevel object which will
#     # be treated as a new window
#


window = Tk()
window.title("Flash Cards")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

canvas_card = Canvas(width=800, height=562, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_background = canvas_card.create_image(400, 263, image=card_front)
card_title = canvas_card.create_text(400, 150, text="Hi", fill='black', font=('Arial', 40, 'italic'))
card_word = canvas_card.create_text(400, 300, text="Salut", font=('Arial', 12, 'bold'))
canvas_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card.grid(row=0, column=0, columnspan=3)

filename = Text(window, width=80, font="Helvetica 12 bold", height=4.5)
filename.grid(row=1, column=0, columnspan=3)

card_right = PhotoImage(file="images/right.png")
known_button = Button(image=card_right, highlightthickness=0, command=check_time)
known_button.grid(row=2, column=0)

card_retry = PhotoImage(file="images/retry.png")
retry_button = Button(image=card_retry, highlightthickness=0, bg='powder blue', command=next_sentence)
retry_button.grid(row=2, column=2)

start = timer()
window.mainloop()
