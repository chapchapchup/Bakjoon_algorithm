s = input()  #단어 입력받기

alphabet = "abcdefghijklmnopqrstuvwxyz"
lista = [-1 for i in range(26)]

for i in range(0,len(s)): #입력한 단어의 길이만큼 반복
    n = alphabet.index(s[i]) #알파벳 번호 찾기
    if lista[n]==-1: #처음 등장한 경우에만 알파벳 위치 저장
        lista[n]= i #lista에서 해당 알파벳 위치

print(str(lista).replace(',','')[1:-1])