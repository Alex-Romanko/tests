with open ('/home/alexandr/Downloads/dataset_3363_3_(1).txt') as inf:
    line = ''
    rows = []
    for line in inf:
        rows.append(line.strip())

new_line = ''
for i in rows:
    new_line = new_line + ' ' + i

a = sorted(new_line.upper().split())


list_a_unrep = set()
for i in a:
    list_a_unrep.add(i)

qaz = sorted(list(list_a_unrep))

q=0
w=0
d = []
for j in qaz:
    q = a.count(j)
    d.append([q, j])

for i in d:
    print (i)



c = (max(d))
qwer = str(c[1]) + ' ' + str(c[0])
print (qwer)

with open ('/home/alexandr/Downloads/answer1.txt', 'w') as ouf:
    ouf.write (qwer)

