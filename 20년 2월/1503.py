n = int(input())

flag = 1
count = 0
for i in range(0,n):
    if flag == 1 :
        if i != 0: 
            count += n
        for j in range(0, n):
            count += 1
            print(count, end =" ")
        flag = -1
    else:
        count += n
        for j in range(n-1, -1, -1):
            print(count, end =" ")
            count -= 1
        flag = 1
    print()