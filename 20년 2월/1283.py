a = int(input())
b = int(input())
bPercent = list(map(int, input().split()))
money = a

for i in bPercent:
    # percent값을 대입하여 구하는 방법!
    # 10000의 10%는 10000 * (1 + 10 / 100)
    # 음수는 음수 그대로 들어감
    margin = a * (1 + i / 100)
    a = margin

left = round(a - money)

if(a > money):
    print("%d"%(left))
    print("good")
elif(a == money):
    print(0)
    print("same")
else:
    print("%d"%(left))
    print("bad")