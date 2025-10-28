def merge_sort(nums):
    print(f"Starting merge sort on: {nums}")
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])
    merged = merge(left_half, right_half)
    print(f"Merged {left_half} and {right_half} into {merged}")
    return merged


def merge(first, second):
    print(f"Merging {first} and {second}")
    sorted_list = []
    i = j = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            sorted_list.append(first[i])
            i += 1
        else:
            sorted_list.append(second[j])
            j += 1
    while i < len(first):
        sorted_list.append(first[i])
        i += 1
    while j < len(second):
        sorted_list.append(second[j])
        j += 1
    print(f"Sorted list so far: {sorted_list}")
    return sorted_list



print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # should return [3, 9, 10, 27, 38, 43, 82]