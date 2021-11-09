nlist = []
alist = []

n, x = input().split()
n = int(n)
x = int(x)

nlist = input().split()

for i in range(0,n):
    if int(nlist[i]) < x:
        alist.append(nlist[i])

print(*alist)