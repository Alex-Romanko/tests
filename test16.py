with open ('/home/alexandr/Downloads/dataset_3363_2_(6).txt') as inf:
    a = inf.readline().strip()

letter_a = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
num_a = '1234567890'
text_a = []
many_a = []
c = []
b = ''
for i in a:
    if i in letter_a:
        text_a.append(i)

for i in a:
    if i in num_a:
        b+=i
    if i not in num_a:
        many_a.append(b)
        b = ''
many_a.append(b)
many_a.pop(0)

for i in many_a:
    c.append(int(i))

q = 0
d = ''
for i in text_a:
    d = d + (i*c[q])
    q+=1
    

print (d)

with open ('/home/alexandr/Downloads/answer1.txt', 'w') as ouf:
    ouf.write (d)

