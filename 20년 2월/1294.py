enList = list(str(input()))

resultList = []

for i in enList:
    if(i == " "):
        resultList.append(' ')
    
    elif(ord(i) >= 120):
        i = ord(i) - 23
        resultList.append(chr(i))
    else:
        i = ord(i) + 3
        resultList.append(chr(i))

for j in resultList:
    if(j == " "):
        print(" ", end="")
    else:
        print(j, end="")