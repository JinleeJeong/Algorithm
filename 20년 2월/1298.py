# 확장 유클리드 호제법

a,b,c = map(int, input().split())
def EEA(a,b):

    # 기본 값을 설정한다.
    c,d = a, b
    x0,x1 = 1, 0
    y0,y1 = 0, 1
    
    
    while(d>0):
        # 1. 몫을 구한다. q
        # 2. 나머지를 구한다. r
        # 3. c는 d값으로 d는 나머지인 r 값으로 대입
        q = c // d
        r = c - q * d
        c,d = d,r
 
        # x 값은 x0 - 몫 * x1 : 나머지 구하는 식이랑 동일
        x = x0 - q * x1
        x0,x1 = x1,x
 
        # y 값은 y0 - 몫 * y1 : 나머지 구하는 식이랑 동일
        y = y0 - q * y1
        y0,y1 = y1,y
 
    print("{} = {}*({}) + {}*({})".format(c, a,x0,b,y0))
 
EEA(a,b) # 7 = 161*(-1) + 28*(6)
