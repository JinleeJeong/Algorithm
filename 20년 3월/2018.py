a, b = map(int, input().split())
start = '1'

def ant_numbers(number, i):
    str_num = ''
    count = 1
    if a-1 == 1 and i == 1:
        print(1)
    
    for idx in range(0, len(number)):

        # idx + 1 == len(number)는 마지막 행을 구한다. count로 쌓인 값 출력
        # number[idx] number[idx+1]은 앞뒤를 비교한다.
        if(idx+1 == len(number)) or number[idx]!=number[idx+1]:
            str_num += str(number[idx]) + str(count)
            count = 1
        else:
            count += 1
    return str_num

if a == 1 and b == 1:
    print(1)
else:
    for i in range(0, b):
        if i >= a-1:
            for j in range(0, len(start)):
                print(start[j], end=" ")
            print()

        start = ant_numbers(start, i)
