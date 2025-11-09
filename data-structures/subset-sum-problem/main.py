def subset_sum(nums, target):
    return find_subset_sum(nums, target, 0)


def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    if index >= len(nums) or target < 0:
        return False

    include_current = find_subset_sum(nums, target - nums[index], index + 1)
    exclude_current = find_subset_sum(nums, target, index + 1)

    return include_current or exclude_current
