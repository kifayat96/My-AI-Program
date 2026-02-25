def find_duplicates(nums):
    duplicates = []
    for n in nums:
        if nums.count(n) > 1 and n not in duplicates:
            duplicates.append(n)
    return duplicates

print(find_duplicates([1,2,3,2,4,1]))
