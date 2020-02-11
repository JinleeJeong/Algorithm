n = int(input())
nDict = dict()
for i in range(0, n):
    #nList 입력
    nList = input()
    
    #띄어쓰기에 따른 key, value
    key, value = nList.split()
    
    #Dictionary에 입력
    nDict[key] = int(value)

# sorted를 통해서 tuple in list로 변환됌.
# dictionary의 item을 넣은 후 [0] [1]로 key, value가 입력됌
# lambda 사용하여, 키를 [1]인 value값 지정
nDict = sorted(nDict.items(), key=lambda k:k[1], reverse=True)

print(nDict[2][0])