triArray = list(map(int, input().split(" ")))

maxLine = 0

for i in triArray:
    if(maxLine < i):
        maxLine = i

triArray.remove(maxLine)

if(maxLine < triArray[0] + triArray[1]):
    print("yes")
else:
    print("no")