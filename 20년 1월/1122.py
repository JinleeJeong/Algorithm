sec = int(input())

minute = 0
if(sec / 60 >= 1):
    minute = sec // 60
    sec = sec % 60
    print(minute, sec, sep=" ")
else:
    print(minute, sec, sep=" ")