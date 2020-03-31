import math

a, b, c = map(int, input().split())

check = b*b - 4 * a * c

if check >= 0:
    
    print('%.2f' %( (-b + math.sqrt(check)) / (2 * a) ))
    if check > 0:
        print('%.2f' %( (-b - math.sqrt(check)) / (2 * a) ))
else:

    h = math.sqrt(-check) / (2 * a)
    if h < 0:
        print('%.2f+%.2fi' %(-b / (2*a), -h))
        print('%.2f%.2fi' %(-b / (2*a), h))
    else:
        print('%.2f+%.2fi' %(-b / (2*a), h))
        print('%.2f%.2fi' %(-b / (2*a), -h))