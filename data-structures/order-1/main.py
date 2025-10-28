def find_last_name(names_dict, first_name):
    if first_name not in names_dict:
        return None
    return names_dict[first_name]

find_last_name({"alice0": "smith0", "bob0": "jones0"}, "bob0")