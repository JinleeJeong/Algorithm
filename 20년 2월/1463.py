n = int(input())

i = 0
j = n
count = 0
while count != n*n:
    if(j > n*n):
        print()
        i += 1
        j = n - i
    else:    
        print(j, end=" ")
        j += n
        count +=1