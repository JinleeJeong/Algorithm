star = int(input())

for i in range(0, star+1):
    print("{}{}".format(" "*i,"*"*(star-i)))