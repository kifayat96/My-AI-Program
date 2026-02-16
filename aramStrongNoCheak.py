def is_armstrong(n):
    total = 0
    temp = n
    power = len(str(n))
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return total == n

print(is_armstrong(153))
