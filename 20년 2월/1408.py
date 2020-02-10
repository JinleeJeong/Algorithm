pwd = list(map(str, input()))
oneArray = []
twoArray = []
for i in pwd:
    oneArray.append(chr(ord(i)+2))
    twoArray.append(chr((ord(i)*7) % 80 + 48))
for i in oneArray:
    print(i, end="")
print()
for j in twoArray:
    print(j, end="")