a, b = map(int, input().split(" "))

if(a % 2 == 0):
    aMessage = "짝수"
else:
    aMessage = "홀수"

if(b % 2 == 0):
    bMessage = "짝수"
else:
    bMessage = "홀수"

if((a+b) % 2 == 0):
    resMessage = "짝수"
else:
    resMessage = "홀수"
print("%s+%s=%s" %(aMessage, bMessage, resMessage))