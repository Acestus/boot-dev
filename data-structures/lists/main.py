def last_work_experience(work_experiences):
    if not work_experiences:
        return None
    return work_experiences[-1]

print("Last work experience:", last_work_experience(['NEC', 'Beacon Hill', 'Microsoft']))