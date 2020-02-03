calculator = str(input())

resultEval = eval(calculator)

if(type(resultEval) == float):
    print("%.2f" %(eval(calculator)))
else:
    print("%d" %(eval(calculator)))
