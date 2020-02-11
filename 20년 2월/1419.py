strList = str(input())

# love lovely 입력
# print 하게 되면, '', ' ', 'ly'가 출력됀다. 
# love로 나누기 때문에 love 앞, love love 사이, love 뒤에가 배열로 쌓인다.
# -1을 해줘야 정확한 값이 출력됀다.
counter = len(strList.split('love'))-1
print(counter)