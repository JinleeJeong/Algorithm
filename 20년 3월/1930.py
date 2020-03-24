import sys

for line in sys.stdin:

    k, n = map(int, line.split())
    array = [[-1]*(n+1) for i in range(k+1)]

    def SuperSum(k, n):
        if k == 0:
            array[0][n] = n
            return n
        
        if array[k][n] == -1:
            mysum = 0
            for i in range(1, n+1):
                mysum += SuperSum(k-1,i)
            
            array[k][n] = mysum
            return mysum
        else:
            return array[k][n]
    print(SuperSum(k,n))

