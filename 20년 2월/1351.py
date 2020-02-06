a, b = map(int, input().split())

if(a == b):
    for i in range(1, 10):
        print("{}*{}={}".format(a,i,a*i))
else :
    for x in range(a, b+1):
        for y in range(1, 10):
            print("{}*{}={}".format(x,y,x*y))