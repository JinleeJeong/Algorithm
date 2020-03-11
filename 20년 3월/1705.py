n = list(str(input()))

count = n.count('3')+n.count('6')+n.count('9')

if count == 0:
    if len(n) == 1:
        print(n[0])
    elif len(n) == 2:
        print(n[0]+n[1])
    else:
        print(n[0]+n[1]+n[2])
else:
    print(count*"K")