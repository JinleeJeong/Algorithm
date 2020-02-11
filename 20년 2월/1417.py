peopleList = list(map(int, input().split()))

peopleList.sort()
print(peopleList[len(peopleList)-3])