nlist = []

try:
    while True:
        a, b = input().split()
        a = int(a)
        b = int(b)
        if a==0 and b==0:
            break
        else:
            nlist.append(a+b)
except:
    for i in range(0,len(nlist)):
        print(nlist[i])

