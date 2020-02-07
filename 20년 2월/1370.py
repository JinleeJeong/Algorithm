h, r = map(int,input().split())
# 3 3
# *
#  *
#   *
#  *
# *
for i in range(0, r):
    count = 0
    for j in range(0, h*2-1):
        if(j >= h):

            print(" "*(count-2), "*", sep="")
            count -= 1
        else:
            print(" "*j, "*", sep="")
            count += 1