dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
w = input() 
r = 0

for i in range(len(w)):
    for j in dial:
        if w[i] in j: 
            r+=dial.index(j)+3

print(r)
    
    
 