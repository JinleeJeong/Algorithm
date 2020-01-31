triArray = list(map(int, input().split(" ")))

maxLine = 0

for i in triArray:
    if(maxLine < i):
        maxLine = i

triArray.remove(maxLine)

print(triArray)