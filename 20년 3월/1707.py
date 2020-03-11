n = list(map(int, input().split()))

winner, loser = 0, 0
nAvg = 0
for i in range(0, len(n)):
    nAvg += n[i]

nAvg /= 10

for i in range(0, len(n)):
    if n[i] >= nAvg:
        winner += 1
    else:
        loser += 1

print(nAvg)
print(winner, loser)