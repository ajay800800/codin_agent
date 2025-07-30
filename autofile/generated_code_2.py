# your python code here
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
i = 2
while len(primes) < 5:
    if is_prime(i):
        primes.append(i)
    i += 1

print(primes)