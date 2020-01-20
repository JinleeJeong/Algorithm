numberArray = list(map(int, input().split(" ")))

for i in numberArray:
    if(i % 2 == 0):
        print("even")
    else:
        print("odd")