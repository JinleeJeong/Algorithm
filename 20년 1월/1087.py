maxNum = int(input())

i = 1
result = 0
while True:
    if(result >= maxNum):
        print(result)
        break
    else:
        result += i 
        i = i + 1