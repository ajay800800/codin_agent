```python
# Python script to print first 5 primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = 2
count = 0
while count < 5:
    if is_prime(num):
        print(num)
        count += 1
    num += 1
```