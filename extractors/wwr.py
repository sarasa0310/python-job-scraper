from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    final_url = f"{base_url}{keyword}"
    print(f"Requesting -> {final_url}")

    response = get(final_url)

    if response.status_code != 200:
        print("Can't get response!")
    else:
        # html 파일을 파싱하여 python 자료구조로 변환
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")

        results = []  # 가공한 job_data를 추가할 빈 리스트

        for job_section in jobs:
            job_posts = job_section.find_all("li")
            job_posts.pop(-1)  # 불필요한 view-all li 태그 제거

            for post in job_posts:
                anchors = post.find_all("a")
                anchor = anchors[1]  # 필요한 a 태그만 가져오기

                title = anchor.find("span", class_="title")
                company, job_type, region = anchor.find_all("span", class_="company")
                link = anchor["href"]

                job_data = {
                    "position": title.string.replace(",", " "),  # .csv 파일에 저장할 것이므로 콤마를 공백으로 대치
                    "company": company.string.replace(",", " "),
                    # "job_type": job_type.string,
                    "location": region.string.replace(",", " "),
                    "link": f"https://weworkremotely.com{link}"
                }
                results.append(job_data)

        return results
