hexi = list(input())

strList = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}

for i in range(0, len(hexi)):
    if hexi[i] in strList:
        print(format(strList.get(hexi[i]), 'b'), end=" ")
    else:
        print(format(int(hexi[i]), 'b').zfill(4), end=" ")