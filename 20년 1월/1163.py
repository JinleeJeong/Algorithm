a,b,c = map(int, input().split(" "))

# 천의 자리를 100으로 나누면(떨어지는 값 생략) 1500 > 15가 되고, 거기서 2로 나눠서 짝수 홀수 비교
result = ((a+b+c) // 100) % 2


if(result == 1):
    print("그럭저럭")
else:
    print("대박")