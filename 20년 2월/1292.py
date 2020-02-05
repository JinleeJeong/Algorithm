dnaNum = list(str(input()))

plusNum = 0
for i in dnaNum:
    plusNum += int(i)

if(plusNum % 7 == 4):
    print("suspect")
else:
    print("citizen")
