n, m = map(int, input().split())

stuInfo = {}
stuArr = []

for i in range(n):
    name, num = input().split()
    stuInfo[i] = {'name' : name, 'num' : int(num)}
    stuArr.append(stuInfo[i])

stuArr = sorted(stuArr, key=lambda e: [-e['num']])

for i in range(0, m):
    print(stuArr[i]['name'])