age = int(input())
year = 2012 - age + 1

if(year >= 2000):
    year -= 2000
    print(year, 3, sep=" ")
else:
    year -= 1900
    print(year, 1, sep=" ")

