time = list(map(int, input().split(".")))

print("%02d" %time[2], "-", "%02d" %time[1], "-", "%04d" %time[0], sep="")