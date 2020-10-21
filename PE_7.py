import math
plist = []
n = 1
primeNum = 1


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1))

while primeNum <= 10001:
    n += 1
    if is_prime(n) == True:
        plist.append(n)
        primeNum += 1  
        
print (max(plist))
