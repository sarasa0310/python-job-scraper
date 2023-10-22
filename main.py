from flask import Flask, render_template, request
from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs


app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="jimmy")


cache = {}  # cache Dictionary


@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    if keyword in cache:
        jobs = cache[keyword]  # 이미 cache에 등록되어 있는 jobs 사용
    else:
        wwr = extract_wwr_jobs(keyword)
        indeed = extract_indeed_jobs(keyword)
        jobs = wwr + indeed
        cache[keyword] = jobs  # cache에 keyword로 등록된 jobs가 없으므로, cache에 새로 등록

    return render_template("search.html",
                           keyword=keyword, jobs=jobs)


app.run(port=9000)
