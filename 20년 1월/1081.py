diceOne, diceTwo = map(int, input().split(" "))

for i in range(1, diceOne+1):
    for j in range(1, diceTwo+1):
        print(i, j)