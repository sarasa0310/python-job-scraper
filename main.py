from selenium import webdriver
from bs4 import BeautifulSoup


# indeed.com의 경우 bot의 접근을 막고 있으므로, selenium을 활용하여 브라우저로 접근
browser = webdriver.Chrome()

base_url = "https://kr.indeed.com/jobs?q="
search_term = "java"

browser.get(f"{base_url}{search_term}")

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="css-zu9cdh eu4oa1w0")  # 채용 공고가 있는 ul 찾기
jobs = job_list.find_all("li", recursive=False)  # 한 단계의 li들만 찾기

results = []  # 가공한 job_data를 추가할 빈 리스트

for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone is None:  # 불필요한 mosaic-zone class div 제외
        anchor = job.select_one("h2 a")

        position = anchor["aria-label"]
        link = anchor["href"]
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")

        job_data = {
            "position": position.rstrip("의 전체 세부 정보"),
            "company": company.string,
            "location": location.string,
            "link": f"https://kr.indeed.com{link}"
        }
        results.append(job_data)

for result in results:
    print(result)
