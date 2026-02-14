def frequency(nums):
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    return freq

print(frequency([1, 2, 2, 3, 1]))
