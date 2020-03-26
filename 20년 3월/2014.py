for a in range(1, 10):
    for b in range(0, 10):
        for c in range(1, 10):
            if (100*a + 10*b + c) - (10*a + b) == (10 * c) + c:
                print("%d%d%d-%d%d=%d%d" %(a,b,c,a,b,c,c))