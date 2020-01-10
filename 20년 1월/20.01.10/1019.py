timeStr = input().split(".")
timeStr[0] = int(timeStr[0])
timeStr[1] = int(timeStr[1])
timeStr[2] = int(timeStr[2])
print("%04d" %timeStr[0],".","%02d" %timeStr[1],"." ,"%02d" %timeStr[2], sep="")

# 0으로 채우고, 4자리 수가 온다는 명시적 표현, %010d 경우에는 10자리 수가 오고 0으로 채운다는 뜻!