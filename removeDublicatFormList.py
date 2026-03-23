def remove_duplicates(nums):
    result = []
    
    for n in nums:
        if n not in result:
            result.append(n)
    
    return result

print(remove_duplicates([1,2,2,3,4,4]))