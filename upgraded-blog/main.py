import requests
from flask import Flask, render_template, request
from post import Post
import smtplib

posts = requests.get("https://api.npoint.io/17e6e02c4cfcaa1fea27").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["author"], post["date"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        data = request.form
        sendto = data['email']
        name = data['name']
        phone_number = data['phone']
        message = data['message']
        my_email = "loooksoook@gmail.com"
        my_pass = "143Muller"
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email, to_addrs=sendto,
                                msg= f"Hey {name},\n"
                                     f"Thank you for visiting thr site\n"
                                     f"Your Number is {phone_number}\n"
                                     f"And you message has been recieved\n"
                                     f"{message}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


# @app.route("/contact", methods=['POST'])
# def receive_data():
#     contact_form = request.form
#     print(contact_form['name'])
#     return "<h1>Successfully sent</h1>"


if __name__ == "__main__":
    app.run(debug=True)

