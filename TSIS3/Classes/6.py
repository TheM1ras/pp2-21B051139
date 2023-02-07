def isPrime(n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = range(100)
# n = int(input())
print(list(filter(lambda n: isPrime(n), numbers)))