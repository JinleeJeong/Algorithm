n = int(input())

i = 1
j = 1
count = 0
while count != n*n:
    if(j > n*n):
        print()
        i += 1
        j = i
    else:    
        print(j, end=" ")
        j += n
        count +=1