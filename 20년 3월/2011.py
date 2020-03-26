a, b = map(int, input().split())

for i in range(a, b+1):
    
    j = i
    cnt = 0
    
    while j > 0:
        if j % 10 == 3 or j % 10 == 6 or j % 10 == 9:
            cnt+=1
        j //= 10
    
    if cnt == 0 :
        print(i)
    else:
        for x in range(0, cnt):
            print("K", end="")
        print()
        