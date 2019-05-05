list = [int(a) for a in input().split()]
i = 0
b = len(list)-1
#print(b)
x = b-1
try:
        c = list[1]+list[-1]
        d = list[b-1]+list[0]

        print(c, end=' ')
        for i in list[1:x]:
                print (list[i-1]+list[i+1], end=' ')
        i +=1
        print(d)
except:
        print(list[0])





