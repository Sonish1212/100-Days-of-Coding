from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_SPEC = ('Arial', 12)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [(random.choice(letters)) for _ in range(random.randint(8, 10))]
    symbols_list = [(random.choice(symbols)) for _ in range(random.randint(2, 4))]
    numbers_list = [(random.choice(numbers)) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char
    password_input.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    try:
        with open('data_file.json', 'r') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error Found", message=f'No file was found')

    else:
        if website_input.get() in data:
            Email = data[website_input.get()['Email']]
            Password = data[website_input.get()['Password']]
            messagebox.showinfo(title=website_input.get(), message=f"Email: {Email}\n Password:{Password}")
        else:
            messagebox.showerror(title='Error catched', message='No such website was stored')
            website_input.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    username = username_input.get()
    password_value = password_input.get()
    pass_dict = {website: {
        "Email": username,
        "Password": password_value
    }}
    # data = file.read(100)
    # if len(data) > 0:
    #     file.write("\n")

    if len(website) == 0 or len(username) == 0 or len(password_value) == 0:
        messagebox.showerror(title="Empty input", message=f"website: {website}\n Email:{username}\n password: "
                                                          f"{password_value}\n, Empty fields are found")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"website: {website}\n Email:{username}\n "
        #                                                       f"password: {password_value}\n Is it ok?")
        #
        try:
            with open('data_file.json', 'r') as data_file:
                data = json.load(data_file)

                # json.dump(pass_dict, data_file, indent=4)
        except FileNotFoundError:
            with open('data_file.json', 'w') as data_file:
                json.dump(pass_dict, data_file, indent=4)

        else:
            data.update(pass_dict)
            with open('data_file.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
# website_label.config(padx=5, pady=5)

website_input = Entry(width=30)
website_input.grid(row=1, column=1)
website_input.focus()

username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0)
# username_label.config(padx=5, pady=5)

username_input = Entry(width=50)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, 'sonishkhanal@gmail.com')

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)
# password_label.config(padx=5, pady=5)

password_input = Entry(width=30)
password_input.grid(row=3, column=1)

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)
# password_button.config(padx=5, pady=5)

add_button = Button(text='Add', width=50, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
# add_button.config(padx=5, pady=5)

search_button = Button(text='Search', width=15, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
