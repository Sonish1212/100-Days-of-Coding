from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/guess/<username>')
def home(username):
    param = {
        "name": username
    }
    response = requests.get("https://api.agify.io", params=param)
    data = response.json()
    guess_age = data["age"]
    user_name = username.title()
    response2 = requests.get("https://api.genderize.io", params=param)
    dat = response2.json()
    guess_gender = dat["gender"]
    return render_template("index.html", name=user_name, age=guess_age, gender=guess_gender)


if __name__ == "__main__":
    app.run(debug=True)


