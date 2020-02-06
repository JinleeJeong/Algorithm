n = int(input())

a,b,c = [], [], []

print("*"*n)
aCount = 0

bCount = 2
bCount_2 = 1

cCount = 0

if(n % 2 == 0):
    for x in range(0,n-2):
        if(n//2-1 <= x):
        
            a.append(aCount)
            aCount-=1

            bCount -= 2
            b.append(n-2-bCount)
            

            c.append(cCount)
            cCount-=1

        else:
            
            a.append(x)
            aCount, cCount = x, x

            b.append(n-2-bCount)

            bCount += 2

            c.append(x)

else:
    for x in range(0,n-2):
        if(n//2-1 < x):
            aCount-=1
            a.append(aCount)
            
            b.append(bCount_2)
            bCount_2 += 2

            cCount-=1
            c.append(cCount)
            
        else:
            a.append(x)
            aCount, cCount = x, x

            if(n-2-bCount == -1):
                b.append(0)
            else:
                b.append(n-2-bCount)
            bCount += 2

            c.append(x)

# 7개의 값 X를 그려야 하기 때문에 대표로 len(a)사용
for i in range(0, len(a)):

    if(n % 2 == 0):
        if(a[i] == 0):
            if(n == 4):
                print("****", sep="", end="")
            else:
                a[i] = 1
                c[i] = 1

                print("*", "*"*a[i], " "*b[i], "*"*c[i] ,"*", sep="", end="")

        elif(b[i] == 0):
            
            print("*", " "*a[i], " "*b[i], "**", " "*c[i] ,"*", sep="", end="")
        else:

            print("*", " "*a[i], "*", " "*b[i], "*", " "*c[i] ,"*", sep="", end="")

    else:    
        if(a[i] == 0):
            if(n == 3):
                print("***", sep="", end="")
            else:
                a[i] = 1
                c[i] = 1

                print("*", "*"*a[i], " "*b[i], "*"*c[i] ,"*", sep="", end="")

        elif(b[i] == 0):
            print("*", " "*a[i], " "*b[i], "*", " "*c[i] ,"*", sep="", end="")
        else:
            print("*", " "*a[i], "*", " "*b[i], "*", " "*c[i] ,"*", sep="", end="")

    print()

print("*"*n)
