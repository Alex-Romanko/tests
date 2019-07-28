with open ('/home/alexandr/Downloads/dataset_3363_3.txt') as inf:
        n = inf.read().lower().split()
a = 0
for i in n:
    if n.count(i) > n.count(a):
        a = i
c = str(a) + ' ' + str(n.count(a))
print (c)

