def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Position,Company,Location,URL\n")  # 컬럼명 작성

    for job in jobs:  # {keyword}.csv 파일에 모든 scarping 결과 작성
        file.write(f"{job['position']},"
                   f"{job['company']},"
                   f"{job['location']},"
                   f"{job['link']}\n")

    file.close()
