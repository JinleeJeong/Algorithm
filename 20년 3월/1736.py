n = int(input())

nDay = 0
nHour = 0
nMinute = 0
nSecond = 0

if n >= 86400:
    nDay += n//86400
    n %= 86400
if n >= 3600:
    nHour += n//3600
    n %= 3600
if n >= 60:
    nMinute += n//60
    n %= 60
nSecond += n

print(nDay, nHour, nMinute, nSecond)