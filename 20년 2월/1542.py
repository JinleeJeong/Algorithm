n = int(input())

def hello(n):
    
    if n % 2 != 0 and n % 3 != 0 :
        print('prime')
    else:
        if n == 1 or n == 2 or n == 3:
            print('prime')    
        else:
            print('composite')
hello(n)