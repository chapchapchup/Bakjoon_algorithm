list1 = []
list2 = []

for i in range(0,10):
    n = int(input())
    list1.append(n%42)

for value in list1:
    if value not in list2:
        list2.append(value)

print(len(list2))