from flask import Flask, render_template, request, redirect, send_file
from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from file import save_to_file


app = Flask("JobScrapper")
cache = {}  # cache Dictionary


@app.route("/")
def home():
    return render_template("home.html", name="jimmy")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")  # 요청 파라미터 가져오기

    if not keyword:  # keyword가 None이거나 빈 문자열인 경우 홈 페이지로 리다이랙트
        return redirect("/")

    if keyword in cache:
        jobs = cache[keyword]  # 이미 cache에 등록되어 있는 jobs 사용
    else:
        wwr = extract_wwr_jobs(keyword)
        indeed = extract_indeed_jobs(keyword)
        jobs = wwr + indeed
        cache[keyword] = jobs  # cache에 keyword로 등록된 jobs가 없으므로, cache에 새로 등록

    return render_template("search.html",
                           keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")

    # 예외 리다이렉트
    if not keyword:  # keyword가 None이거나 빈 문자열인 경우 홈 페이지로 리다이랙트
        return redirect("/")
    if keyword not in cache:
        return redirect(f"/search?keyword={keyword}")

    save_to_file(keyword, cache[keyword])  # {keyword}.csv 파일에 scarping 결과 저장

    return send_file(f"{keyword}.csv", as_attachment=True)  # scraping 결과 파일 반환


app.run(port=9000)
