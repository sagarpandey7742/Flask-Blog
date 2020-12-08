from flask import Flask, render_template, url_for

app = Flask(__name__)

posts=[
    {
        "author":"Sagar Pandey",
        "title":"First Post",
        "content":"First content",
        "date_posted":"December 7 2020"
    },
    {
        "author":"Sagar Pandey 2",
        "title":"Second Post",
        "content":"Second content",
        "date_posted":"December 8 2020"
    },
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html",title="About")


if __name__ == '__main__':
    app.run(debug=True)
