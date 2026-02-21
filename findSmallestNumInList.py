def find_min(nums):
    smallest = nums[0]
    for n in nums:
        if n < smallest:
            smallest = n
    return smallest

print(find_min([4, 2, 9, 1]))