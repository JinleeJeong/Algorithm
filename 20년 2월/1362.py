n=int(input())

count = 0
floor = []

# count로 숫자 for -1을 하기 위한 수 저장
# floor로 배열로 층수 저장
for i in range(1, n+1):
    count+=i
    floor.append(i)

# 층수 만큼 출력!
for x in range(1, len(floor)+1):
    # print('floor[x] : ', floor[x-1], end = " ")
    for y in range(1, floor[x-1] + 1):
        print(count, end=" ")
        count -= 1
    print()