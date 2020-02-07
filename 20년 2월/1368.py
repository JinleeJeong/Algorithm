h, k, d = map(str, input().split())
h = int(h)
k = int(k)
if(d == "L"):
    for i in range(0, h):
        print(" "*i, "*"*k, sep="")
else:
    for j in range(h, 0, -1):
        print(" "*(j-1), "*"*k, sep="")