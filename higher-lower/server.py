import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def guess_number():
    return '<b> Guess a number between 0 to 9</b>' \
           '<br>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def choose_number(number):
    random_num = random.randint(1, 10)
    if random_num > number:
        return '<p style="color: red">Wrong Guess, Too low, Try again </p>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif random_num < number:
        return '<p style="color: red">Wrong Guess, Too high, Try again </p>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif random_num == number:
        return '<p style="color: green">Correct answer!!!</p>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
