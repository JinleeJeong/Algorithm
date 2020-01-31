a,b,c = map(int, input().split())

if(c<a+b):
    if(a == b and a == c):
        print("정삼각형")
    elif((a == b and a != c) or (b == c and b != a) or (c == a and c != b)):
        print("이등변삼각형")
    elif(a ** 2 + b ** 2 == c ** 2):
        print("직각삼각형")
    else:
        print("삼각형")
else:
    print("삼각형아님")