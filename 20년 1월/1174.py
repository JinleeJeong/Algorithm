hour, minute = map(int, input().split(" "))

# getTime은 전체 분으로 계산
getTime=hour*60+minute

# 30분 전을 나타내야함
getTime=getTime-30

# 음수 값이 나올 수 있음. 24 * 60 = 1440을 더함
getTime=24*60+getTime

# 1440으로 다시 나누면 -30분의 결과가 출력
getTime=getTime%(24*60)

hour=getTime//60
minute = getTime % 60
print(hour, minute)