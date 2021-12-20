a, b = input().split()

ra = int(a[2]+a[1]+a[0]) #뒤집기
rb = int(b[2]+b[1]+b[0])

if ra>rb:
    print(ra)
else:
    print(rb)
