plist = []
n = 0
import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1))

while n <= 775147:
    n += 1
    if 600851475143 % n == 0:
        if is_prime(n) == True:
            plist.append(n)

print (max(plist))
