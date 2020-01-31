gameInfo = list(map(int, input().split(" ")))

count = 0
for i in gameInfo:
    if(i == 1):
        count += 1

if(count == 1):
    print("도")
elif(count == 2):
    print("개")
elif(count == 3):
    print("걸")
elif(count == 4):
    print("윷")
else:
    print("모")