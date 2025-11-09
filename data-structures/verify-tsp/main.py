def verify_tsp(paths, dist, actual_path):
    sum_dist = 0
    for i in range(len(actual_path) - 1):
        city_from = actual_path[i]
        city_to = actual_path[i + 1]
        sum_dist += paths[city_from][city_to]
    return sum_dist < dist
