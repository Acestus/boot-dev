def does_name_exist(first_names, last_names, full_name):
    for fn in first_names:
        for ln in last_names:
            candidate = f"{fn} {ln}"
            if candidate == full_name:
                print("Name found!")
                return True
    return False


does_name_exist(["alice", "bob"], ["smith", "jones"], "bob jones")