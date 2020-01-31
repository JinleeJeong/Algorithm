a, b = map(int, input().split(" "))

if(a % b == 0):
    print("%d*%d=%d"%(b, a//b, a))
elif(b % a == 0):
    print("%d*%d=%d"%(a, b//a, b))
else:
    print("none")