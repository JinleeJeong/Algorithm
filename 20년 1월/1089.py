a, d, n = map(int, input().split(" "))
count = 0
resultArray = []

while True:
    
    if count == n:
        print(resultArray[n-1])
        break
    else:
        resultArray.append(a)
        a += d
        count += 1