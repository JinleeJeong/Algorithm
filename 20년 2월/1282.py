n = int(input())

i = 0
nSmall = n
while True:
    
    nSmall = nSmall ** 0.5

    if(nSmall == int(nSmall)):
        print(i, int(nSmall), sep=" ")
        break
    else:
        i += 1
        nSmall = n-i
