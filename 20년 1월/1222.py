time, oneTeam, twoTeam = map(int, input().split())

# 5분마다 한 골씩 넣는다! 90분 전까지
count = 0
while True:
    if(time >= 90):
        break
    else:
        time += 5
        count += 1

oneTeam += count

if(oneTeam > twoTeam):
    print("win")
elif(oneTeam == twoTeam):
    print("same")
else:
    print("lose")