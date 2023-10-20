from selenium import webdriver
from bs4 import BeautifulSoup


# indeed.com의 경우 bot의 접근을 막고 있으므로, selenium을 활용하여 Chrome 브라우저로 접근
browser = webdriver.Chrome()
base_url = "https://kr.indeed.com/jobs"


def get_page_count(keyword):
    browser.get(f"{base_url}?q={keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", class_="ecydgvn0")
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)

    if count == 0:
        return 1
    elif count >= 5:
        return 5
    else:
        return count


def extract_indeed_jobs(keyword):
    page_count = get_page_count(keyword)  # 해당 keyword의 페이지 개수를 가져온다
    print("Found", page_count, "pages")

    results = []  # 가공한 job_data를 추가할 빈 리스트

    for page in range(page_count):  # 페이지 개수만큼 반복
        final_url = f"{base_url}?q={keyword}&start={page * 10}"
        print("Requesting ->", final_url)

        browser.get(final_url)

        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="css-zu9cdh eu4oa1w0")  # 채용 공고가 있는 ul 찾기
        jobs = job_list.find_all("li", recursive=False)  # 한 단계의 li들만 찾기

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

    return results
