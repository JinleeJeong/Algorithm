 
def GCD(a, b):
    if b == None:
        return a
    #처음을 위한 루틴

    if b > a:
        temp = a
        a = b
        b = temp
    #큰 값을 앞에 두기 위한 루틴

    while(b>0):
        temp = b
        b = a%b
        a = temp
    return a

    # 더 작은 값이 0보다 큰 경우
    # 작은 값을 temp
    # b는 a%b
    # a는 temp값 즉 작은 값을 가져옴

def LCM(a,b):
    if b == None:
        return a
    #처음을 위한 루틴

    gcd = GCD(a,b)
    #최소공배수를 위한 값을 구한다.
    a = a // gcd
    b = b // gcd

    #기존의 a b 값에 최소 공배수를 나눈다. //는 나머지도 삭제함
    return (gcd * a * b)
    # 마지막으로 모두 곱해준다.
 
def LCM_args(*args):
    first_LCM = None
    for i in args:
        first_LCM = LCM(i, first_LCM)
 
    return first_LCM
 
 
def GCD_args(*args):
    first_GCD = None
    for i in args:
        first_GCD = GCD(i, first_GCD)
    return first_GCD

print(GCD_args(220,100,58,66))
print(GCD_args(15, 20))

print(LCM_args(15,20,30))
print(LCM_args(15, 20))


# GCD 최대 공약수
# LCM 최소 공배수