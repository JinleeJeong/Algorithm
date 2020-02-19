arrangement = list(str(input()))

result = 0
stick = 0

for i in range(0, len(arrangement)):

    if arrangement[i] == "(":
        stick += 1
    else:
        # 레이저 인 경우, 1빼고 더하기
        if arrangement[i-1] == "(":
            stick -= 1
            result += stick
        # 연속 ))인 경우 1빼고 더하기
        else:
            stick -= 1
            result += 1

print(result)