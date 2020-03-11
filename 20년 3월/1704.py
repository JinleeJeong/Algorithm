a, b = map(int,input().split())
a = list(str(a))
b = list(str(b))

sexFlag = b[:1]

## 01~09년생
if len(a) == 5:
    year = a[:1]

    if int(sexFlag[0]) <= 3:    
        print(12-int(year[0])+101, end=" ")
    else:
        print(12-int(year[0])+1, end=" ")

## 00년생
elif len(a) <= 4:
    year = ['0']

    if int(sexFlag[0]) < 3:    
        print(12-int(year[0])+101, end=" ")
    else:
        print(12-int(year[0])+1, end=" ")

## 나머지
else:
    year = a[:2]

    if int(sexFlag[0]) < 3: 
        print(12-int(year[0]+year[1])+101, end=" ")
    else:
        print(12-int(year[0]+year[1])+1, end=" ")

if int(sexFlag[0])== 1 or int(sexFlag[0]) == 3:
    print("M")
else:
    print("F")