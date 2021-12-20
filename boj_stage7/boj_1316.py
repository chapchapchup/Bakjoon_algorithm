n = int(input()) #입력받을 단어갯수
w_num = [] 
g_num = 0 

for i in range(0,n):
    word = input() #단어 입력받기
    
    for i in range(0,len(word)):
        a = word.index(word[i])
        w_num.append(a) #알파벳 순서 저장 리스트
        
    if sorted(w_num)==w_num: #알파벳 순서가 오름차순이 맞는지 확인
        g_num+=1 #그룹리스트 카운트+1
    
    w_num = [] #알파벳 순서 저장 리스트 초기화
      
print(g_num)
        
    
