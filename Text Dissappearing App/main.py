from tkinter import *
import copy
OCCUR = False


def disappear():
    global current_len, OCCUR, text_box, screen
    new_length = len(text_box.get("1.0", "end"))
    if not OCCUR:
        if new_length == current_len:
            OCCUR = True
            screen.after(3000, disappear)
    elif new_length == current_len and OCCUR:
        text_box.delete("1.0", "end")
        current_len = len(text_box.get("1.0", "end"))
        OCCUR = False
        disappear()
    elif OCCUR:
        current_len = copy.copy(new_length)
        OCCUR = False
        disappear()


screen = Tk()
screen.title("Text Disappearing App")
screen.config(padx=100, pady=50, bg='#417895')
text_label = Label(screen, text="Text Will Disappear in 3 Sec", font=('Century Gothic', 20, 'bold'), bg='#417895', fg='#ffffff')
text_label.grid(row=0, column=0, columnspan=3)
text2_label = Label(screen, text='Type what you want to type in this text box below', font=('Century Gothic', 20, 'bold'), bg='#417895', fg='#ffffff')
text2_label.grid(row=1, column=0, columnspan=3, pady=8)
text_box = Text(screen, width=80, font="Helvetica 12 bold", height=20)
text_box.grid(row=2, column=0, columnspan=3, pady=20)
current_len = len(text_box.get("1.0", "end"))
disappear()
screen.mainloop()