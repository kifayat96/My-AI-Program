def rotate(nums, k):
    n = len(nums)
    k = k % n
    for _ in range(k):
        nums.insert(0, nums.pop())
    return nums

print(rotate([1,2,3,4,5], 2))
