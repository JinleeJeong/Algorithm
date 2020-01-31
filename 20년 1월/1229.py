height, weight = map(float, input().split())

if(height >= 160):
    normalWeight = (height - 100) * 0.9
elif(height >= 150):
    normalWeight = (height - 150) / 2 + 50
else:
    normalWeight = (height - 100)
    
Obesity = (weight - normalWeight) * 100 / normalWeight

if(Obesity > 20):
    print("비만")
elif(Obesity >= 10):
    print("과체중")
else:
    print("정상")