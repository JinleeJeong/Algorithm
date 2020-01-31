num = list(str(input()))


# 한 자리수 
if(len(num) == 1):
    if(num[0] == '1'):
        result = num[0]+"st"
    elif(num[0] == '2'):
        result = num[0]+"nd"
    elif(num[0] == '3'):
        result = num[0]+"rd"
    else:
        result = num[0]+"th"
# 두 자리수 이상
else:
    if(num[0] == '1'):
        result = num[0]+num[1]+"th"
    else:
        if(num[1] == '1'):
            result = num[0]+num[1]+"st"
        elif(num[1] == '2'):
            result = num[0]+num[1]+"nd"
        elif(num[1] == '3'):
            result = num[0]+num[1]+"rd"
        else:
            result = num[0]+num[1]+"th"

print(result)