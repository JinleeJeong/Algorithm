n = int(input())
nList = []

for x in range(0, n):
    nList.append(int(input()))

# 퀵 소트 알고리즘

def quickSort(nList):
    if len(nList) <= 1: return nList

    big_arr, equal_arr, less_arr = [], [], []
    # 가운데 숫자 아무거나 지정
    pivot = nList[len(nList) // 2]

    for i in nList:
        # i가 작으면 less 크면 big
        if i < pivot: less_arr.append(i)
        elif i > pivot: big_arr.append(i)
        else: equal_arr.append(i)
    
    # 재귀함수 사용해서 진행
    return quickSort(less_arr) + equal_arr + quickSort(big_arr)

nList = quickSort(nList)

for i in nList:
    print(i)