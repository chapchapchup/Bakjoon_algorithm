import sys
n = int(input())
nlist1 = []
nlist2 = []

for i in range(0,n):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    nlist1.append(a + b)
    nlist2.append([a, b])

for i in range(0,n):
    print("Case #"+str(i+1)+": "+str(nlist2[i][0])+" + "+str(nlist2[i][1])+" = " + str(nlist1[i]))
