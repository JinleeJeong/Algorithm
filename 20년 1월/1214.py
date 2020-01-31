year, month = map(int, input().split())

if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):

    if(month == 2):
        print('29')
    elif(month in [1,3,5,7,8,10,12]):
        print('31')
    elif(month in [4,6,9,11]):
        print('30')
    else:
        print("?")
else:
    
    if(month == 2):
        print('28')
    elif(month in [1,3,5,7,8,10,12]):
        print('31')
    elif(month in [4,6,9,11]):
        print('30')
    else:
        print("?")