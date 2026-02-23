def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)

print(average([2, 4, 6, 8]))