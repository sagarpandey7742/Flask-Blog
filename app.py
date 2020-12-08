from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2ade7dca04722e1dc2aa38dd6c31023898993cf0291432e811cee85e3526e898'
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
    print(form.validate_on_submit())
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}.", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = RegistrationForm()
    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
