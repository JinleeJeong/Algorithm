a, b, c = map(int, input().split())

if b%2 == 0:
    print("%d%d%d %d%d%d" %(a,b,c,a,b,c))
else:
    print("%d%d%d" %(a,b,c))