n = int(input())

def hello(n):
    if n < 0:
        print('negative')
    elif n == 0:
        print('zero')
    else:
        print('positive')
hello(n)