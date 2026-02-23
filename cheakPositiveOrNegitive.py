def check_numbers(nums):
    for n in nums:
        if n >= 0:
            print("Positive")
        else:
            print("Negative")

check_numbers([3, -1, 5, -2])