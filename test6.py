a = int(input())
if (a + 4) % 5 == 0 and (a -1) % 5 == 0 and (a -1) % 2 == 0 and (a - 11) % 100 != 0:
    print(a,"программист")
elif (a % 2 == 0 and (a + 3) % 5 == 0 and (a - 12) % 100 != 0):
    print(a, "программиста")
elif (a + 2) % 5 == 0 and (a - 3) % 5 == 0 and (a - 3) % 2 == 0 and (a -13) % 100 != 0:
    print(a, "программиста")
elif a % 2 == 0 and (a + 1) % 5 == 0 and (a - 4) % 5 == 0 and (a - 14) % 100 != 0:
    print(a, 'программиста')
else:
    print(a, 'программистов')

