x = 0
y = 0

for i in range(1,101):
    x = i**2
    y += x
    #print(y)

a = 0
b = 0

for i in range(1,101):
    a = a + i
    b = a**2
    #print(b)

print(b - y)
