c = []
while True:
    a = input().split()
    if a[0] != 'end':
        a = [int(i) for i in a]
        c.append(a)
        x = len(a)
    else:
        break
l = len(c)
new = [[sum([c[i-1][j], c[(i+1)%l][j], c[i][j-1], c[i][(j+1)%x]]) for j in range(x)] for i in range(l)]
for i in range (l):
    for j in range (x):
        print(new[i][j], end =' ')
    print()
