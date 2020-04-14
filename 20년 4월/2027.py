n = int(input())

cornWay = [1, 1]

for i in range(n-2):
    idx = cornWay[len(cornWay)-1]
    first = cornWay[idx-1]
    second = cornWay[len(cornWay)-idx]

    sumNum = first+second
    cornWay.append(sumNum)
    # print(cornWay)

print(cornWay[len(cornWay)-1])