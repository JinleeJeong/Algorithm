n, k = map(int,input().split())

nk = n // k

if nk > 9999:
    print("번호 초과 오류")
else:
    for i in range(0, nk):
        print("F-%04d" %(i+1))