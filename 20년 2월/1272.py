k, h = map(int, input().split())

john = 0
bob = 0

if(k % 2 == 0):
    john = k * 5
else:
    john = k // 2 + 1
if(h % 2 == 0):
    bob = h * 5
else:
    bob = h // 2 + 1
    
print(john+bob)