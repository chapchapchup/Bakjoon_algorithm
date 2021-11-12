n = int(input()) 
nlist = input().split() 
nlist = list(map(int, nlist)) #리스트 형변환

a = nlist[0]
b = a

for i in range(0,n):
    if a>nlist[i]: #리스트에서 가장 작은 숫자 찾기
        a = nlist[i]

    if b<nlist[i]: #리스트에서 가장 큰 숫자 찾기
        b = nlist[i]

print(a, b)



