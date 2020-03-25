k = int(input())
List = list(input())

for i in range(0, len(List)):
    S = 3*(i+1) + k
    # print("S", S)
    # print("ord", ord(List[i]), List[i])
    if ord(List[i]) - S < 65:
        # print("Over")
        print(chr(ord(List[i])-S+26), end="")
    else:
        # print("Not Over")
        print(chr(ord(List[i])-S), end="")

