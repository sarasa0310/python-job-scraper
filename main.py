from flask import Flask

app = Flask("JobScrapper")


@app.route("/")
def home():
    return "hey there!"


app.run(port=9000)
