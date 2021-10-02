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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_timer(long_break_min)
        label.config(text="Long Break", fg=RED, bg=YELLOW)

    elif reps % 2 == 0:
        count_timer(short_break_min)
        label.config(text="Short Break", fg=PINK, bg=YELLOW)

    else:
        count_timer(work_min)
        label.config(text="Work time", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_timer(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_timer, count - 1)
    else:
        start_count()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

label = Label(text="Timer", font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)
label.grid(column=2, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill='white', font=(FONT_NAME, 40, 'bold'))
canvas.grid(column=2, row=2)

button_start = Button(text="Start", font=(FONT_NAME, 16, 'bold'), fg=GREEN, bg=RED, command=start_count)
button_start.grid(column=1, row=3)

button_reset = Button(text="Reset", font=(FONT_NAME, 16, 'bold'), fg=GREEN, bg=RED, command=reset_timer)
button_reset.grid(column=3, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=3)

window.mainloop()
