def is_hansu(n): #input : 수(100~999범위), return : 한수 여부
    nlist = list(str(n))
    
    a = int(nlist[0]) #백
    b = int(nlist[1]) #십
    c = int(nlist[2]) #일

    if a-b==b-c:
        return True
    else:
        return False    
    
    
def hansu_count(n):#input : 범위, return : 범위 내 한수의 개수
    counter=0
    
    if 99<n<1000:
        for i in range(100,n+1):
            if is_hansu(i):
                counter+=1
        counter += 99
    elif n<100:
        counter = n
    else:
        counter = 144
        
    return counter


n = int(input())
print(hansu_count(n))