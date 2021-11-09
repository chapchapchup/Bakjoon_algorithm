a, b = input().split()
a = int(a)
b = int(b)

if b<45:
    if a==0:
        a = 23
        b += 15
    else:
        a -= 1
        b += 15
else:
    b -= 45

print(a, b)