daenamu = int(input())

count = 0
for i in range(1, daenamu):
    if(daenamu % i == 0):
        count += 1

print(count)