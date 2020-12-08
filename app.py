from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '2ade7dca04722e1dc2aa38dd6c31023898993cf0291432e811cee85e3526e898'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    img = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User ({self.username}, {self.email},{self.img})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post ({self.title}, {self.date_posted})"


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


if __name__ == '__main__':
    app.run(debug=True)
