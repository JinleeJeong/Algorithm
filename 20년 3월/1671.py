m, c = map(int,input().split())

def rsp(m, c):
    if m == c:
        print("tie")
    else:
        if (m == 0 and c == 1) or (m == 1 and c == 2) or (m == 2 and c == 0):
            print("win")
        else:
            print("lose")

rsp(m,c)