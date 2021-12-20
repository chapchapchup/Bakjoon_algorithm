s = input()
croatia= ["c=","c-","dz=","d-","lj","nj","s=","z="] #크로아티아 알파벳

for i in croatia:
    if i in s: #입력한 문자열에서 크로아티아 알파벳 찾기
        s=s.replace(i,".") #찾은 크로아티아 알파벳을 .으로 변환
    
print(len(s)) 