n = int(input())

nList = []
resultList = []
cnt = 0
for i in range(n):
    nList.append(input())

for i in nList:

    if len(list(i)) <= 3:
        cnt += 1
        resultList.append(i)
    elif 'tap' in i:
        cnt += 1
        resultList.append(i)
    elif 'xocure' in i:
        cnt += 1
        resultList.append(i)
    else:
        continue

for i in resultList:
    print(i)

if len(resultList) >= 7:
    print("danger")
elif len(resultList) >= 4:
    print("warning")
else:
    print("safe")