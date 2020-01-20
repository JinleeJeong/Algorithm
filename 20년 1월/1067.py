number = int(input())

if number > 0:
    print("plus")
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("minus")
    if number % 2 == 0:
        print("even")
    else:
        print("odd")