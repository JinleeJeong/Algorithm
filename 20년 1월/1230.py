a, b, c = map(int, input().split())

crashNum = 0
if( a <= 170 ):
    print("CRASH %d"%a)
elif( b <= 170):
    print("CRASH %d"%b)
elif( c <= 170):
    print("CRASH %d"%c)
else:
    print("PASS")