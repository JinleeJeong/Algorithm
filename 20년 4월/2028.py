k = int(input())
cnt = 0
sumNum = 0

i = 1
while cnt <= k:

    cnt = 0
    sumNum += i
    
    j = 1
    while j*j <= sumNum:
        if sumNum % j == 0:
            if sumNum != j*j:
                cnt += 2
            else:
                # 1이 되입 된 경우 +=1
                cnt += 1

        j+=1
    i += 1
     
print(sumNum)