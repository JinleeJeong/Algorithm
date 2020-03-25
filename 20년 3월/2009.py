K, N = map(int, input().split())

Coupon = K
othCoupon = 0
Coffee = 0

while 1:
    if Coupon >= N: # Coupon 10 N 3
        if Coupon % N == 0:
            # print("하위", Coffee, Coupon)
            Coffee += Coupon // N
            Coupon = Coupon // N
        else:
            # print("바위", Coffee, Coupon)
            Coffee += Coupon // N
            nowCoffee = Coupon // N
            for i in range(Coupon, -1, -1):
                if i % N == 0:
                    Coupon = Coupon - i
                    Coupon += nowCoffee
                    break
    else:
        break
print(Coffee)