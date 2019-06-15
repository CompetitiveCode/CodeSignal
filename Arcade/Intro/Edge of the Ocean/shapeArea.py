#Answer to shapeArea - https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ

def shapeArea(n):
    return sum(((2*i)-1)*2 for i in range(1,n))+(2*n)-1
