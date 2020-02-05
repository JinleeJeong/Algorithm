n = int(input())

x = 0
y = 0
j = 0
maxNum = 0
resultNum = 0
# i는 2부터 중간 값까지의 값을 가져서 i+i+j+j가 성립하도록 j를 구한다.
for i in range(2, n//2):
    
    # j의 값은 중간값(소수 포함 - i)로 만약 n의 값이 7이면, i는 2, j는 1.5가 됀다.
    j = n/2 - i
    
    if(i+i+j+j == n):
        
        if(maxNum < i*j):
            maxNum = i*j
            resultNum = i

print(resultNum)
