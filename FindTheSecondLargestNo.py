def second_largest(nums):
    first = second = float('-inf')
    
    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
    
    return second

print(second_largest([10, 20, 4, 45, 99]))