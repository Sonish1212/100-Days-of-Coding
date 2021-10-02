from form import LoginForm, RegisterForm, TodoForm
from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", '8BYkEfBA6O6donzWlSihBXox7C0sKR6b')
ckeditor = CKEditor(app)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///todo.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.__init__(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class TodoList(db.Model):
    __tablename__ = "Todo_list"
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(250), unique=True, nullable=False)
    complete = db.Column(db.Boolean)

    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("Users.id"))
    # Create reference to the User object, the "posts" refers to the posts property in the User class.
    author_post = relationship("User", back_populates="posts")


class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(500), nullable=False)

    # This will act like a List of TodoList objects attached to each User.
    # The "author" refers to the author property in the TodoList class.
    posts = relationship("TodoList", back_populates="author_post")
db.create_all()




@app.route('/')
def get_all_posts():
    posts = TodoList.query.all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("Sorry the user has not been registered!!")
            return redirect(url_for("login"))

        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("get_all_posts"))
        else:
            flash("sorry the user's password is wrong please try again!!")
            return redirect(url_for('login'))

    return render_template("login.html", logged_in=current_user.is_authenticated, form=form, current_user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':

        if User.query.filter_by(email=request.form.get('email')).first():
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_salt_password = generate_password_hash(
            password=request.form.get('password'),
            method="pbkdf2:sha256",
            salt_length=8
        )

        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_salt_password
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/make-todo', methods=['GET', 'POST'])
def create_todo():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = TodoList(
            todo=form.todo.data,
            author_id=current_user.id,
            complete=False
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-todo.html", form=form, current_user=current_user)

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = TodoList.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = TodoList.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    app.run(debug=True)
