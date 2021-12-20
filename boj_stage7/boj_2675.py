n = int(input()) #테스트케이스 개수 입력받기 

for i in range(n): #테스트케이스 개수만큼 반복
    r, s = input().split() #r = 문자 반복 횟수, s=문자열
    r = int(r) 
    result = "" #결과
    
    for i in range(0,len(s)):
        result += s[i]*r #r만큼 반복후 결과에 더하기
        
    print(result)
    
