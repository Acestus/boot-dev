def bubble_sort(nums):
    print(f"Starting bubble sort on: {nums}")
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    print(f"Sorted list: {nums}")
    return nums


bubble_sort([5, 7, 3, 6, 8])  # should return [3, 5, 6, 7, 8]