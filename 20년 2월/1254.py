a, b = map(str, input().split())

aOrd = ord(a)
bOrd = ord(b)

for i in range(aOrd, bOrd):
    print(chr(i), end= " ")