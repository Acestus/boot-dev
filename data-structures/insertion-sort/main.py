def insertion_sort(nums):
    print(f"Starting insertion sort on: {nums}")
    for i in range(1, len(nums)):
        print(f"I: {i}")
        j = i
        while j > 0:
            print(f"I: {i} and J: {j}")
            print(f"First Value: {nums[j-1]}")
            print(f"Second Value: {nums[j]}")
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    print(f"Sorted List: {nums}")
    return nums

insertion_sort([5, 2, 0, 1])