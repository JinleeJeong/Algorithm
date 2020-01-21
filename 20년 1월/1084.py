rgbArray = list(map(int, input().split(" ")))

count = 0
for x in range(rgbArray[0]):
    for y in range(rgbArray[1]):
        for z in range(rgbArray[2]):
            count = count+1
            print("%d %d %d" %(x, y, z))

print(count)