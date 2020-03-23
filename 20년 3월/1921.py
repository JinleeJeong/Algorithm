n, k = map(int ,input().split())

def change(x, y):
    if x == 0:
        return
    # print('x: y: ',x, y)
    change(x//y, k)

    if(x%y < 10):
        # print("one")
        print("%d"%(x%y), end="")
    elif x%y >= 10:
        # print("two")
        print("%c" %(x%y+55), end="")

change(n,k)