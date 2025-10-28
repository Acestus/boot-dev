def average_followers(nums):
    print(f"Calculating average for followers: {nums}")
    print(f"Number of entries: {len(nums)}")
    print(f"Sum of followers: {sum(nums)}")
    if not nums:
        return None
    return sum(nums) / len(nums)



average_followers([100, 200, 300])