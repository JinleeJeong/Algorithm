n = int(input())

def hello(n):
    
   
    for i in range(2, n):
        if n % i == 0:
            return print("composite")
    print("prime")
hello(n)