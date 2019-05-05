list = [int(a) for a in input().split()]
num = int(input())
res =[]
q = 0
for a in list:
    if num == a:
        res.append(q)
        q+=1
    else:
        q +=1
x = len(res)-1

z = 0
if res == []:
    print('Отсутствует')
else:
    while z <= x:
        print(res[z], end=' ')
        z+=1
