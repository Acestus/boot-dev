def exponential_growth(n, factor, days):
    result = []
    current = n
    for day in range(days + 1):
        result.append(current)
        current *= factor
    return result

print(exponential_growth(10, 2, 5))