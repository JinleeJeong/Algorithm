chNum = input()

bjFlag = True

frontSum = 12
BackSum = 1

split = chNum.split("H")
split[0] = split[0].replace("C", "")

if split[0] == '' and split[1] == '':
    print(frontSum+BackSum)
elif split[0] == '':
    print(frontSum+BackSum*int(split[1]))
elif split[1] == '':
    print(frontSum*int(split[0])+BackSum)
else:
    print(frontSum*int(split[0])+BackSum*int(split[1]))