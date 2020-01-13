a,b,c,d,e = list(map(int, input()))

print('[', a*10000, ']', sep="")
print('[', b*1000, ']', sep="")
print('[', c*100, ']', sep="")
print('[', d*10, ']', sep="")
print('[', e*1, ']', sep="")

# map은 새로운 객체를 만들어, list 배열로 저장한다.
# a,b,c,d,e로 각 배열의 값을 할당받는다.