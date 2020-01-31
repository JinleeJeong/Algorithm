menuList = list(map(int,input().split()))

resultCalorie = 0
for i in menuList:
    if(i == 1):
        resultCalorie += 400
    elif(i == 2):
        resultCalorie += 340
    elif(i == 3):
        resultCalorie += 170
    elif(i == 4):
        resultCalorie += 100
    elif(i == 5):
        resultCalorie += 70

if(resultCalorie > 500):
    print("angry")
else:
    print("no angry")