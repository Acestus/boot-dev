def tsp(cities, paths, dist):
    all_permutations = permutations(cities)
    for perm in all_permutations:
        sum_dist = 0
        for i in range(len(perm) - 1):
            city_from = perm[i]
            city_to = perm[i + 1]
            index_from = cities.index(city_from)
            index_to = cities.index(city_to)
            sum_dist += paths[index_from][index_to]
        if sum_dist < dist:
            return True
    return False

# don't touch below this line


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res
