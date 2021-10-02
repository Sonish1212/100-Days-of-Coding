from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import glob

SOURCE_DIRECTORY = 'E:/New folder'
BACKGROUND_COLOR = "#B1DDC6"
TARGET_DIRECTORY = 'E:/from day 24 python/watermark app/saved_image'


def open_file():
    file_img = askopenfilename(initialdir=SOURCE_DIRECTORY, title="Select A File",
                               filetype=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    img = ImageTk.PhotoImage(Image.open(file_img))
    canvas_card.create_image(200, 200, anchor=NW, image=img)
    if file_img:
        photo = Image.open(file_img)
        w, h = photo.size
        # make the image editable
        drawing = ImageDraw.Draw(photo)
        font = ImageFont.truetype("Roboto-Black.ttf", 68)

        # get text width and height
        text = "© " + "Sonish Khanal" + "   "
        text_w, text_h = drawing.textsize(text, font)

        pos = w - text_w, (h - text_h) - 250

        c_text = Image.new('RGB', (text_w, text_h), color='#000000')
        drawing = ImageDraw.Draw(c_text)

        drawing.text((0, 0), text, fill="#ffffff", font=font)
        c_text.putalpha(250)

        photo.paste(c_text, pos, c_text)
        photo.save(file_img)

    photo_list = glob.glob('python_images/in/*.*')
    for photo in photo_list:

        out = photo.replace('in', f'{TARGET_DIRECTORY}/image.png')
        open_file()



window = Tk()
window.title("Flash Cards")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

canvas_card = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")

card_background = canvas_card.create_image(400, 263, image=card_front)

canvas_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card.grid(row=0, column=0, columnspan=3)
btn = Button(text='select image', width=10,
             height=1, bd='2', command=open_file)
btn.grid(row=0, column=1)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=2)

card_right = PhotoImage(file="images/right.png")
known_button = Button(image=card_right, highlightthickness=0)
known_button.grid(row=1, column=0)

window.mainloop()
