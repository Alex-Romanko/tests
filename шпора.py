#НИЧЕГО НЕ СТИРАТЬ
'''
пробегает по всем элементам в двумерном массиве, заканчивается, когда находит значение, записанное в b
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
b = 0
for i in range(len(a)):
    if b == 3:
        break
    for j in range(len(a[i])):
        b = a[i][j]
        if b == 3:
            break        
        print(b)
'''



''' можно вводить строки через пробел, создает одномерный массив (b+=a), двумерную матрицу (c.append(a)) заканчивает считывать при вводе end
b =[]
c =[]
while True:
    a = input().split()
    x = (a)
    print(x[0])
    if x[0] != 'end':
        b+=a
        c.append(a)
    else:
        break
print ('eeeeeeeeeee')
print (b)
print (c)

print("******************")
#печатает отдельные символы в виде таблицы, второй принт нужен для перехода на новую строку после окончания печати каждого вложенного списка
for i in c:
    for j in i:
        print(j, end=' ')
    print()


print("******************")
#печатает списки в виде таблицы, каждый список с новой строки
for i in c:
    print (i)

'''




'''   
при добавлении новой пары ключ: значение в словарь нужно просто записать
словарь[key]=(valye) либо = [valye] для добавление списка как значение


d = {12: [-1, -2]}
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif 2*key in d:
        d[2*key].append(value)
    else:
        d[2*key]=[value]
    return d



update_dictionary(d, 2, -2)
print (d)

'''