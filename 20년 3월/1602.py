n = float(input())

def abs(n):
    
    if n >= 1000000 or n < -1000000:
        
        if n < 0:
            print("%.10g" %-n)
        else:
            print("%.10g" %n)
    else:
        if n < 0:
            print("%g" %-n)
        else:
            print("%g" %n)

abs(n)