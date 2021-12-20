s = input()
a = s.count(" ")+1 #띄어쓰기 세기

if s[0]==" ": 
    a-=1  #앞에 공백이 있을때

if s[len(s)-1]==" ":
    a-=1 #뒤에 공백이 있을때
    
print(a)

