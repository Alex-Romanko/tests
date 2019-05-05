a = int(input())
b = int(input())
c = int(input())


if a == b and c < a:
    print(a)
    print(c)
    print(b)
elif a == c and b < a:
    print(a)
    print(b)
    print(c)
elif b == c and a < b:
    print(b)
    print(a)
    print(c)
elif a == b and b == c:
    print(a)
    print(b)
    print(c)
elif a > b and b == c:
    print(a)
    print(b)
    print(c)
elif b > a and a == c:
    print(b)
    print(a)
    print(c)
elif c > a and a == b:
    print(c)
    print(a)
    print(b)
elif a > b and a > c and c < b:
    print(a)
    print(c)
    print(b)
elif a > b and a > c and b < c:
    print(a)
    print(b)
    print(c)
elif b > a and b > c and a < c:
    print(b)
    print(a)
    print(c)
elif b > a and b > c and c < a:
    print(b)
    print(c)
    print(a)
elif c > a and c > b and a < b:
    print(c)
    print(a)
    print(b)
elif c > a and c > b and b < a:
    print(c)
    print(b)
    print(a)

