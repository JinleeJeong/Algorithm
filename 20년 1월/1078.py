intNum = int(input())
i = 1
resultNum = 0
while i <= intNum:
    
    if(i % 2 == 0):
        resultNum = resultNum + i
        i = i + 1
    else:
        i = i + 1
        continue
    
    
print(resultNum)