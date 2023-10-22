from flask import Flask, render_template, request
from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="jimmy")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    wwr = extract_wwr_jobs(keyword)
    indeed = extract_indeed_jobs(keyword)
    jobs = wwr + indeed

    return render_template("search.html",
                           keyword=keyword, jobs=jobs)


app.run(port=9000)
