def primes_upto(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(primes_upto(20))
