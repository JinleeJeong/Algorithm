n = int(input())
nArray = []
resultArray = []

for i in range(0, n-1):
    card = int(input())
    nArray.append(card)

for i in range(1, n+1):
    if i not in nArray:
        print(i)
        