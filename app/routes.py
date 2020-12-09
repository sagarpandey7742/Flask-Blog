from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user, logout_user, login_required

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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}.", category="success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f"Logged in successfully", category="success")
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for("home"))
        else:
            flash(f"Login Unsuccessful, enter correct credentials", category="danger")
    return render_template('login.html', title="Login", form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash(f"Logged out successfully", category="success")
    return redirect(url_for("home"))


@app.route('/account')
@login_required
def account():
    return render_template("account.html", title="Account")
