S1 = input()
S2 = input()
S3 = input()

cycleFlag = True


if S1[len(S1)-1] == S2[0] and S2[len(S2)-1] == S3[0] and S3[len(S3)-1] == S1[0]:
    print('good')
else:
    print('bad')         