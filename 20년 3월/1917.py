n, k = map(int, input().split())

multi = n
kCnt = 1
def nk(k, kCnt):
    # print(k, kCnt)
    global multi
    if kCnt != k:
        multi *= n
        kCnt += 1
        # print(multi, kCnt)
        nk(k, kCnt)
    
if k == 0 or n == 1:
    print(1)
elif n == -1 and k % 2 == 0:
    print(1)
elif n == -1 and k % 2 != 0:
    print(-1)
else:
    nk(k, kCnt)
    print(multi)
