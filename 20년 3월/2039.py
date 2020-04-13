import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

startHour, startMinute, studyRange, breakTime, studyCount, n, lunchTime = map(int,input().split())

cnt = 0

for i in range(1, n+1):
    
    # end에서 쉬는시간 더해서, start 구하기!
    if i == 1:
        # 첫 endHour endMinute 구하기
        if startMinute + studyRange >= 60:
            endHour = startHour + 1
            endMinute = startMinute + studyRange - 60
        else:
            endHour = startHour
            endMinute = startMinute + studyRange
    else:
        if endMinute + breakTime >= 60:
            endHour += 1
            endMinute = endMinute + breakTime - 60
        else:
            endMinute = endMinute + breakTime

        startHour = endHour
        startMinute = endMinute

        # end 구하기
        if startMinute + studyRange >= 60:
            endHour = startHour + 1
            endMinute = startMinute + studyRange - 60
        else:
            endHour = startHour
            endMinute = startMinute + studyRange

    cnt += 1

    print('%d:%02d-%d:%02d %d교시' %(startHour, startMinute, endHour, endMinute, cnt), end="")    
    print()

startHour = endHour
startMinute = endMinute

# end 구하기
# print(startMinute, lunchTime)
if lunchTime > 60:
    endHour += lunchTime // 60
    lunchTime = lunchTime % 60


    if startMinute + lunchTime >= 60:
        endHour +=1
        endMinute = startMinute + lunchTime - 60
    else:
        endMinute = startMinute + lunchTime

else:
    if startMinute + lunchTime >= 60:
        endHour = startHour + 1
        endMinute = startMinute + lunchTime - 60
    else:
        endHour = startHour
        endMinute = startMinute + lunchTime

# print(startMinute, lunchTime)

print('%d:%02d-%d:%02d 점심시간' %(startHour, startMinute, endHour, endMinute), end="")  
print()

for i in range(cnt, studyCount):
    
    # end에서 쉬는시간 더해서, start 구하기!
    if i == cnt:
        
        startHour = endHour
        startMinute = endMinute

        # 첫 endHour endMinute 구하기
        if startMinute + studyRange >= 60:
            endHour = startHour + 1
            endMinute = startMinute + studyRange - 60
        else:
            endHour = startHour
            endMinute = startMinute + studyRange
    else:

        if endMinute + breakTime >= 60:
            endHour += 1
            endMinute = endMinute + breakTime - 60
        else:
            endMinute = endMinute + breakTime

        startHour = endHour
        startMinute = endMinute

        # end 구하기
        if startMinute + studyRange >= 60:
            endHour = startHour + 1
            endMinute = startMinute + studyRange - 60
        else:
            endHour = startHour
            endMinute = startMinute + studyRange

    print('%d:%02d-%d:%02d %d교시' %(startHour, startMinute, endHour, endMinute, i+1), end="")    
    print()
