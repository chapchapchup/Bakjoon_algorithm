a = input()
b = input()
a = int(a)
b = int(b)

x = (b//100) #b,백
y = (b//10)-(x*10) #b,십
z = b-(x*100)-(y*10) #b,일

print(a*z)
print(a*y)
print(a*x)
print(a*b)