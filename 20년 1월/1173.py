hour, minute = map(int, input().split(" "))

# 0분을 넘어 시가 바뀜
if(minute <= 29):
    minute = minute + 30
    
    if(hour == 0):
        hour = 23
    else:
        hour -= 1
# 30분을 넘어 시가 바뀌지 않음
else:
    minute = minute - 30

print(hour, minute, sep=" ")

