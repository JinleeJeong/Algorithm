n = int(input())

def toChar(number):
    # print(number)
    if number > 0:
        number -= 1
        toChar(number//26)
        print(chr(number%26 + 65), end="")

toChar(n)
