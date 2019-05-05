a = int(input())
b = int(input())
c = int(input())


if a == b and c < a:
    print ( a + '\n' + c + '\n' + b)
elif a == c and b < a:
    print ( a + '\n' + b + '\n' + c)
elif b == c and a < b:
    print ( b + '\n' + a + '\n' + c)

elif a > b and a > c and c < b:
    print ( a + '\n' + c + '\n' + b)
elif a > b and a > c and b < c:
    print ( a + '\n' + b + '\n' + c)

elif b > a and b > c and a < c:
    print ( b + '\n' + a + '\n' + c)


elif b > a and b > c and c < a:
    print( b + '\n' + c + '\n' + a)


elif c > a and c > b and a < b:
    print( c + '\n' + a + '\n' + b)


elif c > a and c > b and b < a:
    print( c + '\n' + b + '\n' + a)

