def first_unique(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        if count == 1:
            return nums[i]
    return None

print(first_unique([2, 3, 4, 2, 3, 5]))