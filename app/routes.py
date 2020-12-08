from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post


posts = [
    {
        "author": "Sagar Pandey",
        "title": "First Post",
        "content": "First content",
        "date_posted": "December 7 2020"
    },
    {
        "author": "Sagar Pandey 2",
        "title": "Second Post",
        "content": "Second content",
        "date_posted": "December 8 2020"
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}.", category="success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "sagarpandey7742@gmail.com" and form.password.data == "admin":
            flash(f"Successfully logged in.", category="success")
            return redirect(url_for("home"))
        else:
            flash(f"Login Unsuccessful", category="danger")
    return render_template('login.html', title="Login", form=form)
