a, b = map(float, input().split())

a = round(a * 100)
b = round(b * 100)

for i in range(a, b+1):
    if(i == 0):
        print("%.2f" %-(i/100), end=" ")
    else:
        print("%.2f" %(i/100), end = " ")