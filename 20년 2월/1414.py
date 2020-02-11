clist = list(str(input()))

cCount = 0
ccCount = 0
for i in clist:
    if ord(i) == 99 or ord(i) == 67:
        cCount += 1
    
for i in range(0, len(clist)-1):
    if (ord(clist[i]) == 99 or ord(clist[i]) == 67) and (ord(clist[i+1]) == 99 or ord(clist[i+1]) == 67):
        ccCount += 1

print(cCount)
print(ccCount)