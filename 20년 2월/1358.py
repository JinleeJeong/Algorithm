n = int(input())

blankCount = 0
if(n % 2 == 1):
    for i in range(1, n+1):
        if(i % 2 == 1):
            blank = (n-i)//2
            # print(blank)
            print("."*blank, end=" ")
            print("{}".format("*"*i))