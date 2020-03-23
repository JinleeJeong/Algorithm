N = list(input())

oppoList = ""
cnt = len(N)-1

def opposit(cnt):
    global oppoList
    if cnt >= 0:
        oppoList += N[cnt]
        cnt -= 1
        opposit(cnt)

opposit(cnt)
print(int(oppoList))