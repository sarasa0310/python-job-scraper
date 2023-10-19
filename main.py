from extractors.wwr import extract_wwr_jobs


jobs = extract_wwr_jobs("python")
for job in jobs:
    print(job)
