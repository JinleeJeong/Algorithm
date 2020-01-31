noIncome, Income, cost = map(int, input().split())

if(noIncome > Income-cost):
    print("do not advertise")
elif(noIncome == Income-cost):
    print("does not matter")
else:
    print("advertise")