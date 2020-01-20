wantedChar = list(map(str, input().split(" ")))

for i in wantedChar:
    if(i == 'q'):
        print('q')
        break
    else:
        print(i)