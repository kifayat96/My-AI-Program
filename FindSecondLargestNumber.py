def second_largest(nums):
    largest = second = float('-inf')
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n > second and n != largest:
            second = n
    return second

print(second_largest([4, 8, 1, 9, 6]))
