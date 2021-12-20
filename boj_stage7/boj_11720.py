n = int(input()) #숫자 갯수 입력
nlist = input() #숫자 입력
sumn = 0 #합계

for i in range(0,n):
    sumn += int(nlist[i]) #숫자 더하기
    
print(sumn)