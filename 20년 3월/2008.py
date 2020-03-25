import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())
nList = list(map(int, input().split()))

nCont = ""
nFlag = ""

# 모두 같은 값이 나오면 섞임으로 처리 하나라도 다르면, 그에 대한 답
allSame = []

# 전체 루틴
for i in range(0, n-1):
    # print("Here : ",nCont, nFlag, i)

    if nList[i] < nList[i+1]:
        allSame.append(1)
        if i == 0:
            nCont = "오름차순"
        
        # 내림차순인 경우 믹스 처리 공백이였으면, 결국 같은 값이였다는 뜻
        elif nCont != "오름차순" and nCont != "":
            nFlag = "Mix"
        else:
            nCont = "오름차순"

    # 같으면 allSame 리스트 담기 + 기존의 nCont 가져오기
    elif nList[i] == nList[i+1]:
        allSame.append(0)
        if i != 0:
            nCont = nCont
    else:
        allSame.append(1)
        if i == 0:
            nCont = "내림차순"
        elif nCont != "내림차순" and nCont != "":

            nFlag = "Mix"
        else:
            nCont = "내림차순"


# allSame List에 모두 0이면, 섞임 처리, 아니면 nCont 처리
for i in range(0, len(allSame)):
    if allSame[i] == 1 and i != len(allSame) -1:
        break
    elif i == len(allSame) -1 and allSame[i] == 0:
        nFlag = "꽝"
        
# 그냥 섞인 경우
if nFlag == "Mix":
    print("섞임")
#모두 0인 경우
elif nFlag == "꽝":
    print("섞임")
else:
    print(nCont)
    