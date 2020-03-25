a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
Nikky = 0
Byron = 0

cnt = 0
whileAB = True
whileCD = True

while 1:
    if whileAB == False:
        break
    else:
        for i in range(a):
            # print(s, cnt)
            if s == cnt:
                whileAB = False
                break
            else:
                Nikky += 1
                cnt += 1

        for j in range(b):
            if s == cnt:
                whileAB = False
                break
            else:
                Nikky -= 1
                cnt += 1

cnt = 0

while 1:
    if whileCD == False:
        break
    else:
        for i in range(c):
            if s == cnt:
                whileCD = False
                break  
            else:
                Byron += 1
                cnt += 1

        for j in range(d):
            if s == cnt:
                whileCD = False
                break
            else:
                Byron -= 1
                cnt += 1
        
if Nikky > Byron:
    print("Nikky")
elif Nikky == Byron:
    print("Tied")
else:
    print("Byron")