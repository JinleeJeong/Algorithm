strList = list(str(input()))

for idx, value in enumerate(strList):
    if value == 't':
        print(idx+1, end=" ")