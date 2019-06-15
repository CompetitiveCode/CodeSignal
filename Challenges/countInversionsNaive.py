# Answer to countInversionsNaive
# https://app.codesignal.com/challenge/j4tsozmpSzHSzS8sF


#80
a = eval(dir()[0])[0]
return sum(1 for i,x in enumerate(a) for y in range(i,len(a)) if x>a[y])

#83
#def countInversionsNaive(a):
#    return sum(1 for i,x in enumerate(a) for y in range(i,len(a)) if x>a[y])

#88
#def countInversionsNaive(a): return sum(1 for i,x in enumerate(a) for y in range(i,len(a)) if x>a[y])

#96
#def countInversionsNaive(a):
#    r = 0
#    l = len(a)
#    for i,x in enumerate(a):
#        for y in range(i,l):
#            if x>a[y]:
#                r += 1
#    return r
