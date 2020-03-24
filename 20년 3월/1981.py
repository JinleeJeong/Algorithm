import os
currentPath = os.getcwd()
f = open(currentPath+"\\secret.dic\\", 'r')
s = f.read()
print(s)