i = int(input())
list = []
for j in range(i+1):
    list += [str(j)]*j
    print (list)
for j in range(i):
    print(list[j], end=' ')