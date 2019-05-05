# високосный год

a = int(input())
b = a % 4
c = a % 100
d = a % 400

print(b)
print(c)
print(d)


if b == 0 and c != 0 or d == 0:
    print ('Високосный')
else:
    print ('Обычный')



