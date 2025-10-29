def power_set(input):
    if len(input) == 0:
        return [[]]
    first = input[0]
    rest_power_set = power_set(input[1:])
    with_first = [[first] + subset for subset in rest_power_set]
    return rest_power_set + with_first



power_set([1, 2, 3])