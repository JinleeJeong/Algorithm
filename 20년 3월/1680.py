for s in range(1, 10):
    for o in range(0, 10):
        for t in range(1, 10):
            if s*10+o+s*10+o == t*100+o*10+o:
                print("%d%d+%d%d=%d%d%d" %(s,o,s,o,t,o,o))