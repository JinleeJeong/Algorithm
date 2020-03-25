aList = ["*", "x", "*"]
bList = [" ", "x", "x"]
cList = ["*", " ", "*"]

k = int(input())

for i in range(k):
    for j in range(3):
        print(aList[j]*k, end="")
    print()

for i in range(k):
    for j in range(3):
        print(bList[j]*k, end="")
    print()

for i in range(k):
    for j in range(3):
        print(cList[j]*k, end="")
    print()