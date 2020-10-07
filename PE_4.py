pallist = []
for x in range(1,1000):
    for y in range(1,1000):
        num = x * y
        rev = int(str(num)[::-1])
        if num == rev:
            pallist.append(rev)
print (max(pallist))
