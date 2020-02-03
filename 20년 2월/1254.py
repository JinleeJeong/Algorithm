a, b = map(str, input().split())

aOrd = ord(a)
bOrd = ord(b)

for i in range(aOrd, bOrd+1):
    print(chr(i), end= " ")