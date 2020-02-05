enList = list(str(input()))

resultList = []

for i in enList:
    #대문자
    if(ord(i) < 97):
        i = i.lower()
        resultList.append(i)
    #소문자
    else:
        i = i.upper()
        resultList.append(i)

for j in resultList:
    print(j, end="")