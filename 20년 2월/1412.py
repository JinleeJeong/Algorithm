from collections import OrderedDict
# collections OrderedDict를 써야 순서 보장 (Python 버전별 문제)
inputString = list(str(input()))

resultDic = OrderedDict(sorted({
    'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0
}.items()))
# items를 넣지 않으면, unpack 예외가 발생
for i in inputString:
    if(ord(i) >= 97 and ord(i) <= 122):
        if i in resultDic.keys() :
            resultDic[i] += 1

for key,value in resultDic.items():
    print(key, ':', value, sep="")