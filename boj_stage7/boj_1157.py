s = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lista = [0 for i in range(26)]

for i in range(0,len(s)): #입력한 단어의 길이만큼 반복
    x = alphabet.index(s[i].upper()) #입력 알파벳 대문자로 변경 & 번호 찾기 
    lista[x]+=1 #알파벳 갯수 구하기
    
maxn = max(lista) #리스트내 가장 큰 수 구하기

if lista.count(maxn)!=1: #갯수가 많은 알파벳이 여러개일 경우
    print("?")
else:
    y = lista.index(maxn)
    print(alphabet[y]) #가장 갯수가 많은 알파벳 출력
s = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lista = [0 for i in range(26)]

for i in range(0,len(s)): #입력한 단어의 길이만큼 반복
    x = alphabet.index(s[i].upper()) #알파벳 번호 찾기
    lista[x]+=1
    
maxn = max(lista)

if lista.count(maxn)!=1:
    print("?")
else:
    y = lista.index(maxn)
    print(alphabet[y])