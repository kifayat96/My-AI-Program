def multiply(nums):
    result = 1
    for n in nums:
        result *= n
    return result

print(multiply([2, 3, 4]))
