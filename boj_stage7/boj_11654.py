n = input() #값 받기
listA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #대문자 리스트
lista = "abcdefghijklmnopqrstuvwxyz" #소문자 리스트
list1 = "0123456789" #숫자 리스트

if n.isupper():
    print(listA.index(n)+65) #대문자 아스키 번호 65~90
elif n.islower():
    print(lista.index(n)+97) #소문자 아스키 번호 97~122
else:
    print(list1.index(n)+48) #숫자 아스키 번호 48~57
    
#print(ord(n)) 으로도 해결 가능