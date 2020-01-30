a, b = map(int, input().split(" "))
# a 주민번호 b 현재 나이 c 주민번호의 앞 2자리
compareYear = list(str(a))
# Python 문법 상, 맨 앞 List에 문자열 0이 담기면 삭제 됌 길이로 조건 판단

# 1900년생
if(b == 1 or b == 2):

    c = (a // 10000) + 1900
    print(2012-c+1)

# 2000년생
else:
    # 01~1x 년생
    if(len(compareYear) in [5,6]):
        c = (a // 10000) + 2000
        print(2012 - c + 1)
    # 00년생
    elif(len(compareYear) == 4):
        c = 2000
        print(2012 - c + 1)
        
    else:
        c = 2000
        print(2012 - c + 1)

