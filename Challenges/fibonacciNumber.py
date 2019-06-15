# Answer to fibonacciNumber
# https://app.codesignal.com/challenge/hTvQiQuJTk9bSvY6n

def f(n):
    return n if n < 2 else f(n-1) + f(n-2)

return f(eval(dir()[0])[0])
