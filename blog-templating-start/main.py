import requests
from flask import Flask, render_template

from post import Post

posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog_posts=post_objects)


if __name__ == "__main__":
    app.run(debug=True)
