a, b = map(int, input().split())
c, d = map(int, input().split())

# d * 2개씩 출력 후, b만큼(열) 하고
# 그걸 c만큼 하고 그걸 a만큼 함

for i in range(a):
    for j in range(c):
        for x in range(b):
            for y in range(d):
                if x % 2 == 0:
                    if i % 2 == 0:
                        print("X", end="")
                    else:
                        print(".", end="")
                else:
                    if i % 2 == 0:
                        print(".", end="")
                    else:
                        print("X", end="")
        print()