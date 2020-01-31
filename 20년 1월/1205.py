x, y = map(float, input().split(" "))

numArray = []
a = x+y
b = y+x
c = x-y
d = y-x
e = x*y
f = y*x
g = x / y
h = y / x
i = int(x) ** int(y)
j = int(y) ** int(x)

numArray.extend((a,b,c,d,e,f,g,h,i,j))
maxNum = 0
for num in numArray:

    if(maxNum < num):
        maxNum = num

print("%.6f" %maxNum)