a, b, c = list(map(int, input().split(" ")))

resultOne = a+b+c
resultTwo = (a+b+c)/3

print("%d" %resultOne, "%.1f" %resultTwo, sep="\n")