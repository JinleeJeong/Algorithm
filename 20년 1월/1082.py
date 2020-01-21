decimal = input()

decimal = int(decimal, 16)
for x in range(1, 16):
    print("%X*%X=%X" %(decimal, x, decimal * x))