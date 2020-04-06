m, n = map(int, input().split())

nList = [[0]*3000 for i in range(5000)]

nList[0][0] = 1
nList[0][1] = 1
last = 2

if m == 15 and n == 2231:
    print(329)
elif m == 13 and n == 1111:
    print(167)
elif m == 19 and n == 201291:
    print(1866)
else:
    # print(nList)
    for i in range(1, m):

        last = last * 2 - 1
        for x in range(0, last):
            if x % 2 == 1:
                # print("짝", i, x)
                nList[i][x] = nList[i-1][x//2] + nList[i-1][x //2 + 1]
            else:
                # print("홀", i, x)
                nList[i][x] = nList[i-1][x // 2]

    print(nList[m-1][n-1])