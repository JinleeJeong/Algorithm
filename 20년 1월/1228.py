height, weight = map(float, input().split())

normalWeight = (height - 100) * 0.9
Obesity = (weight - normalWeight) * 100 / normalWeight

if(Obesity > 20):
    print("비만")
elif(Obesity >= 10):
    print("과체중")
else:
    print("정상")