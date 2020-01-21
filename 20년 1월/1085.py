h, b, c, s = map(int, input().split(" "))

result = (h*b*c*s) / (8*1024*1024)

# 8을 나눈 이유는 bit > Byte를 위함이고 1024는 Byte 단위 중, B -> KB -> MB를 위함이다.
    
print("%.1f MB" %result)