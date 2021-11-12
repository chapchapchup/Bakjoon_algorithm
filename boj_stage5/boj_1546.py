list1 = []
list2 = []
m = 0
result = 0 

n = int(input()) #과목 개수 받기
list1 = input().split() #성적 리스트로 받기
list1 = list(map(int,list1)) #리스트 형 int로 변환

for i in range(0,n): #최고점수 구하기
    if m<list1[i]:
        m = list1[i]    

for value in list1: #성적 새로 구하기
    list2.append(value/m*100)

for i in range(0,n): #새로운 성적 모두 더하기
    result += list2[i]
    
print(result/n) #모두 더한 성적 나눠서 평균 구하기