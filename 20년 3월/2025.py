dateStr = input()

dateList = dateStr.split("/")

year = dateList[0]
monthDay = dateList[1]+dateList[2]
Flag = True

for i in range(0, len(year)):
    if year[i] in monthDay:
        # print("yes", year[i])
        monthDay = monthDay.replace(year[i], "", 1)
    else:
        # print("no", year[i])
        Flag = False
    
if Flag:
    print("yes")
else:
    print("no")