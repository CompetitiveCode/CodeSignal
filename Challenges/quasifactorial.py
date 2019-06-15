# Answer to quasifactorial
# https://app.codesignal.com/challenge/53DMcWRBbZMdsF6vm

def f(n):
    return 1 if n<2 else n * f(n-1) -1

n = eval(dir()[0])[0]
return f(n)
