time, score = map(int, input().split(" "))

if(time % 5 == 0):
    adding = ((90-time) // 5)
else:
    adding = ((90-time) // 5) + 1
print(adding+score)