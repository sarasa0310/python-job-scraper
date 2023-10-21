from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs

keyword = input("What do you want to search for?(ex. python, java, spring...)")

wwr = extract_wwr_jobs(keyword)  # we_work_remotely.com job scraping
indeed = extract_indeed_jobs(keyword)  # indeed.com job scraping

jobs = wwr + indeed  # scraping 결과 list 병합

file = open(f"{keyword}.csv", "w")
file.write("Position,Company,Location,URL\n")  # 컬럼명 작성

for job in jobs:  # {keyword}.csv 파일에 모든 scarping 결과 작성
    file.write(f"{job['position']},"
               f"{job['company']},"
               f"{job['location']},"
               f"{job['link']}\n")

file.close()
