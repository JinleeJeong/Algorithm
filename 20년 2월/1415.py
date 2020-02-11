numList = list(map(int, input().split()))

oddNum = 0
evenNum = 0

for i in numList:
    if i%2 == 1:
        if oddNum < i:
            oddNum = i
    else:
        if evenNum < i:
            evenNum = i
if(oddNum == 0):
    print(evenNum)
elif(evenNum == 0):
    print(oddNum)
else:
    print(oddNum, evenNum)

