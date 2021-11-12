bonus = 0 #O연속 점수 
score = 0 #ox 점수
oxlist = [] #ox 리스트
scorelist = [] #점수 저장 리스트

n = int(input()) 

for i in range(0,n):
    x = input()
    oxlist = list(x)#ox 리스트 생성
    
    for i in range(0,len(oxlist)):
    
        if oxlist[i]=="O": #인수가 O인 경우
            bonus+=1 
            score += bonus
        else: #인수가 X인 경우
            bonus = 0
    
    scorelist.append(score) #점수 리스트에 점수 저장하기
    bonus = 0 #O연속 점수
    score = 0 #ox 점수
    
    
for value in scorelist:
    print(value)   
    
          
  
    
    
    
