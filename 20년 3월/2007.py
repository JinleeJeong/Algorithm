n = int(input())
nList = list(map(int, input().split()))

nCont = ""
nFlag = ""
for i in range(0, n-1):
    if nList[i] < nList[i+1]:
        if i == 0:
            nCont = "오름차순"
        elif nCont != "오름차순":
            nFlag = "Mix"
    else:
        if i == 0:
            nCont = "내림차순"
        elif nCont != "내림차순":
            nFlag = "Mix"

if nFlag == "Mix":
    print("섞임")
else:
    print(nCont)