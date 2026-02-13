def find_max(nums):
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
    return m

print(find_max([3, 7, 2]))
