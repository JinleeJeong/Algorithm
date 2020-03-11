n = int(input())

h, m, s = 0, 0, 0
if n // 3600 >= 1:
    h = n//3600
    n = n%3600
if n // 60 >= 1:
    m = n//60
    n = n%60

s = n

print(h, m, s)