from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs

keyword = input("What do you want to search for?(ex. python, java, spring...)")

wwr = extract_wwr_jobs(keyword)  # we_work_remotely.com job scraping
indeed = extract_indeed_jobs(keyword)  # indeed.com job scraping

jobs = wwr + indeed  # scraping 결과 list 병합
for job in jobs:
    print(job)  # scraping 결과 출력
