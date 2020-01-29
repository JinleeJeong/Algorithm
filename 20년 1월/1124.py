A = list(input())
# 입력 받은 정보를 리스트!

arr1 = []
counter = 0
arr2 = []
# arr1 arr2로 H를 기준으로 배열 분해 with Counter


resultA = 0
resultB = 0

for x in A:
    if(x == "H"):
        break
    else:
        arr1.append(x)
        counter += 1

for i, v in enumerate(A):
    if(i < counter):
        continue
    else:
        arr2.append(v)
# 분해하는 로직

whileVarA = 0
whileVarB = 0
# while문의 각 arr index 역할하는 변수

while True:
    # 만약 C의 값이 나오면 index 값 증가 후 continue
    if(arr1[whileVarA] == "C"):
        whileVarA += 1
        continue
    # array length로 판단 2~4까지 총 1~100까지의 수가 입력되어, 한번 루틴 후 종료
    else:
        if(len(arr1) == 2):
            resultA = arr1[whileVarA]
        elif(len(arr1) == 3):
            resultA = arr1[whileVarA] + arr1[whileVarA+1]
        else:
            resultA = arr1[whileVarA] + arr1[whileVarA+1] + arr1[whileVarA+2]
        break

while True:
    
    if(arr2[whileVarB] == "H"):
        whileVarB += 1
        continue
    else:
    
    # array length로 판단 2~4까지 총 1~100까지의 수가 입력되어, 한번 루틴 후 종료
        if(len(arr2) == 2):
            resultB = arr2[whileVarB]
        elif(len(arr2) == 3):
            resultB = arr2[whileVarB] + arr2[whileVarB+1]
        else:
            resultB = arr2[whileVarB] + arr2[whileVarB+1] + arr2[whileVarB+2]
        break

# C값 대입
print((12*int(resultA))+int(resultB))