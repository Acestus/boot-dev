def quick_sort(nums, low, high):
    print("Quick Sort called on:", nums[low:high + 1])
    if low < high:
        partition_index = partition(nums, low, high)
        quick_sort(nums, low, partition_index - 1) 
        quick_sort(nums, partition_index + 1, high)
    return nums


def partition(nums, low, high):
    print("Partitioning:", nums[low:high + 1])
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
    print("Partitioned to:", nums[low:high + 1], "with pivot", pivot)
    return i + 1


print("Sorted array is:", quick_sort([10, 7, 8, 9, 1, 5], 0, 5))


