def make_num(n): #input:생성자, return:생성자로 만든 수
    num = 0
    nlist = list(str(n))
    
    for i in range(0,len(nlist)):
        num += int(nlist[i])
        
    return num+n


def num_list_make(n): #input:범위, return: input 범위내 생성자로 만든 수 리스트
    num_list = []
    
    for i in range(1,n):
        if make_num(i)<n:
            num_list.append(make_num(i))
            
    return(num_list)


def find_self(n): #input:범위, return: input 범위내 셀프 넘버 리스트
    num_list = num_list_make(n)
    self_list = []
    
    for i in range(1,n):
        if i not in num_list:
            self_list.append(i)
            
    return(self_list)
            
            
result = find_self(10000)   
for i in range(0,len(result)):
    print(result[i])
    
    

    
        
