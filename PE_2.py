x = 0
y = 1
res = 0
while x < 4000000:
    y = x + y
    x = y - x
    if y % 2 == 0:
        res += y
print(res)
