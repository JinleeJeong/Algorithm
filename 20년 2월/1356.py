star = int(input())

for i in range(1, star+1):
    if(i == 1 or i == star):
        print("{}".format("*"*star))
    else:
        print("{}{}{}".format("*"," "*(star-2),"*"))