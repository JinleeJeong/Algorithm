n = int(input())

num = n / 4

# 0을 만드는 모든 수 예외처리!
if(n % 4 == 0):
    print(int(num*num))

# .5를 만드는 모든 수 예외처리
elif(int(num*10) == num * 10):

    num = int(num)
    print((num*(num+1)))
# .75를 만드는 모든 수 예외처리
else:   
    num = int(num) 
    print(int(num*(num+1.5)))

