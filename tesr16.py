a = sorted(input().upper().split())
list_a_unrep = sorted(list(set(a)))
q=0
for j in list_a_unrep:
    q = a.count(j)
    print(j + ' ' + str(q))




