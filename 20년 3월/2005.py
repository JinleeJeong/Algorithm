n = int(input())
aList = list(map(int, input().split()))
m = int(input())
aFlag = False

for i in range(0, n):
    for j in range(1, n):

        if (abs(aList[i] - aList[j])) % m == 0 and aList[i] != aList[j]:
            # print(aList[i], aList[j])
            aFlag = True
            break
        else:
            continue

if aFlag == True:
    print("no")
else:
    print("yes")