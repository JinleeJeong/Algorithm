n = int(input())

a,b,c = [], [], []

print("*"*n)
aCount = 0

bCount = 2
bCount_2 = 1

cCount = 0

# 홀수는 테두리를 기준으로 X줄과 십자가를 만든다!

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

# print(a,b,c)
# 7개의 값 X를 그려야 하기 때문에 대표로 len(a)사용
for i in range(0, len(a)):
    
    if(a[i] == 0):
        if(n == 3):
            print("***", sep="", end="")
        else:
            a[i] = 1
            c[i] = 1
            midStar = 1
            print("*", "*"*a[i], " "*(b[i]//2), "*"*midStar, " "*(b[i]//2),  "*"*c[i] ,"*", sep="", end="")

    elif(b[i] == 0):
        print("*"*n, sep="", end="")
    else:
        midStar = 1
        print("*", " "*a[i], "*", " "*(b[i]//2), "*"*midStar, " "*(b[i]//2), "*", " "*c[i] ,"*", sep="", end="")


    print()

print("*"*n)
