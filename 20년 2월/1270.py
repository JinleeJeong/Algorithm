n = str(input())

count = 0
for i in range(1, int(n)+1):
    numList = list(str(i))
    if(numList[len(numList)-1] == '1'):
        count += 1
    
print(count)