def find_max(nums):
    print(f"Finding max in list: {nums}")
    if not nums:
        return None
    max = float('-inf')
    print(f"Initial max value set to: {max}")
    for num in nums:
        if num > max:
            max = num
            print(f"New max found: {max}")
    print(f"Final max value: {max}")
    return max



find_max([7, 4, 3, 100, 2343243, 343434, 1, 2, 32])