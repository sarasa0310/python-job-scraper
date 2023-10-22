from flask import Flask, render_template

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="jimmy")


@app.route("/hello")
def hello():
    return "hello!"


app.run(port=9000)
