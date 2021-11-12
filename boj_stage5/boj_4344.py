n = int(input()) #케이스 수
p_list=[]

for _ in range(n):
    c_list = list(map(int,input().split())) #케이스 리스트
    avg =sum(c_list[1:])/c_list[0]#케이스 평균 
    a_avg = 0
    
    for value in c_list[1:]:
        if value>avg:
            a_avg+=1 #평균을 넘는 학생수 구하기
    
    rate = a_avg/c_list[0]*100
    p_list.append('{0:0.3f}%'.format(rate))#비율 구해서 저장하기

for value in p_list: 
    print(value) #비율 리스트 출력

            
    
    
    
