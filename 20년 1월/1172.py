a,b,c = list(map(int, input().split(" ")))

sortedArray = []

if(a == b == c):
    sortedArray.append(a)
    sortedArray.append(b)
    sortedArray.append(c)

elif(a == b):
    if(a < c):
        sortedArray.append(a)
        sortedArray.append(b)
        sortedArray.append(c)
    else:
        sortedArray.append(c)
        sortedArray.append(a)
        sortedArray.append(b)

elif(b == c):
    if(a < b):
        sortedArray.append(a)
        sortedArray.append(b)
        sortedArray.append(c)
    else:
        sortedArray.append(b)
        sortedArray.append(c)
        sortedArray.append(a)
elif(a == c):
    if(a < b):
        sortedArray.append(a)
        sortedArray.append(c)
        sortedArray.append(b)
    else:
        sortedArray.append(b)
        sortedArray.append(a)
        sortedArray.append(c)
elif(a < b):
    if(b < c):
        sortedArray.append(a)
        sortedArray.append(b)
        sortedArray.append(c)
    else:
        sortedArray.append(a)
        sortedArray.append(c)
        sortedArray.append(b)
elif(b < c):
    if(c < a):
        sortedArray.append(b)
        sortedArray.append(c)
        sortedArray.append(a)
    else:
        sortedArray.append(b)
        sortedArray.append(a)
        sortedArray.append(c)
elif(c < a):
    if(a < b):
        sortedArray.append(c)
        sortedArray.append(a)
        sortedArray.append(b)
    else:
        sortedArray.append(c)
        sortedArray.append(b)
        sortedArray.append(a)

for i in sortedArray:
    print(i, end=" ")
       


    
