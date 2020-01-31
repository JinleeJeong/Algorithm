trash = list(str(input()))

resultNum = int(trash[1]+trash[0]) * 2

if(resultNum > 100):
        resultNum -= 100

if(resultNum <= 50 ):
    print(resultNum,"GOOD",sep="\n")
else:
    
    print(resultNum,"OH MY GOD",sep="\n")