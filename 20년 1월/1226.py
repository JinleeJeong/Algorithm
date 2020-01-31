lottoNum = list(map(int, input().split()))

customerNum = list(map(int, input().split()))

bonusNum = lottoNum[len(lottoNum)-1]
lottoNum.pop()
count = 0
bonusCount = 0
# 보너스 카운트는 한번만 가능하게 저장 (2등을 위함)

for i in lottoNum:
    for j in customerNum:    
        if(i == j):        
            count += 1
        if(bonusCount == 0):
            if(bonusNum == j):            
                bonusCount += 1

if(count == 6):
    print("1")
elif(count == 5 and bonusCount == 1):
    print("2")
elif(count == 5):
    print("3")
elif(count == 4):
    print("4")
elif(count == 3):
    print("5")
else:
    print("0")