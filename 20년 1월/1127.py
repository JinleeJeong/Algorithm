testResult = []

for i in range(0, 3):
    testResult.append(list(map(float,input().split(" "))))

# print("testResult : ", testResult)
result = (testResult[0][0] * testResult[0][1]) + (testResult[1][0] * testResult[1][1]) + (testResult[2][0] * testResult[2][1])

print("%.1f" %result)