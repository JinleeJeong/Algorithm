a, b = map(int, input().split())

result = []
resultNum = 0
for i in range(a,b+1):
    if(i % 2 == 0):
        resultNum -= i
        result.append('-'+str(i))
    else:
        resultNum += i
        result.append('+'+str(i))

for j in result:
    print(j, end="")
print("=%d" %(resultNum))