n = int(input())
nList = list(map(int, input().split()))
k = int(input())

def codeup(n, nList, k):
    for idx, i in enumerate(nList):
        if i > k:
            return idx+1

result = codeup(n, nList, k)
if result == None:
    print(len(nList)+1)
else:
    print(result)