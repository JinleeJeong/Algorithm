from math import *

x1, y1=map(int, input().split())
x2, y2=map(int, input().split())

dx=x1-x2
dy=y1-y2

print("%.2lf"%(sqrt(dx*dx + dy*dy)))