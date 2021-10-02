from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    button_start(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def button_start(count):
    canvas.itemconfig(time, text={})
    if count > 0:
        window.after(1000, button_start, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title('Pomodoro')

timer_label = Label(text='Timer', font=(FONT_NAME, 46, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=1)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(101, 112, image=tomato_image)
time = canvas.create_text(100, 110, text='00:00', fill='white', font=(FONT_NAME, 32, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=RED, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=RED)
reset_button.grid(row=2, column=3)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(row=2, column=1)



window.mainloop()