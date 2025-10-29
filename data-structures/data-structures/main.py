def count_marketers(job_titles):
    target = "marketer"
    count = 0
    for title in job_titles:
        if title.lower() == target:
            count += 1
    return count

print("Counting marketers in:", count_marketers(["developer", "marketer", "designer"]))
