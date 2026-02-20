def missing_number(nums, n):
    total = n * (n + 1) // 2
    for num in nums:
        total -= num
    return total

print(missing_number([1,2,4,5], 5))
