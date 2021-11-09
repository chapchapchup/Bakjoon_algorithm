t = int(input())
tlist = []

for i in range(0,t):
    a, b = input().split()
    a = int(a)
    b = int(b)
    tlist.append(a+b)

for i in range(0,t):
    print(tlist[i])