import copy

n = int(input())
nList = list(map(int, input().split()))
mList = copy.copy(nList)
mList = sorted(mList)
cnt = 0

def binary_search(arr, value):
    low = 0
    high = len(arr)-1
    while (low <= high):
        mid = (low+high)//2
        
        if arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        else:
            return mid
        
    return -1

for i in nList:
    print(binary_search(mList, i), end=" ")
