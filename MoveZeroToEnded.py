def move_zeros(nums):
    result = []
    
    for n in nums:
        if n != 0:
            result.append(n)
    
    for n in nums:
        if n == 0:
            result.append(n)
    
    return result

print(move_zeros([0,1,0,3,12]))