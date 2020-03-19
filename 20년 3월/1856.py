n = int(input())

def stair(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1 + stair(1)
    elif n == 3:
        return 1 + stair(1) + stair(2)
    else:
        return stair(n-3) + stair(n-2) + stair(n-1)

print(stair(n))