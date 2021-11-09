x = int(input()) 
y = x
n = 0 #사이클 수 

while True:
    a = y//10 #십의 자리
    b = y%10 #일의 자리
    c = (a+b)%10
    y = b*10+c
    n+=1

    if x==y:
        break

print(n)