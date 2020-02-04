n = int(input())

i = 0
nSmall = n
while True:
    # nSmall의 제곱근을 구한다.    
    nSmall = nSmall ** 0.5

    # 만약 제곱근의 값이 int형이라면 나누어 지는 것이기 때문에 출력 후 종료
    if(nSmall == int(nSmall)):
        print(i, int(nSmall), sep=" ")
        break
    # 그게 아니라면, nSmall 값(n)을 하나씩 줄인다.
    else:
        i += 1
        nSmall = n-i
