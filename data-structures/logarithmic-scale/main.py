def log_scale(data, base):
    import math
    scaled_data = []
    for value in data:
        log_value = math.log(value, base)
        scaled_data.append(log_value)
    print(f"Data: {data}")
    print(f"Base: {base}")
    print(f"Scaled data (before rounding): {scaled_data}")
    return scaled_data


log_scale([1, 10, 100, 1000], 10)