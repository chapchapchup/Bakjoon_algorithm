import sys

n = int(input())
nlist = []

for i in range(0,n):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    nlist.append(a+b)

for i in range(0,n):
    print(nlist[i])