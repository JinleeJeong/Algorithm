index = int(input())

for x in range(1, index+1):
    if(x % 3 == 0):
        print("X", end=" ")
    else:
        print(x, end=" ")