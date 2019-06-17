# Answer to evenDigitsOnly
# https://app.codesignal.com/challenge/nckaDwhQf2gb4HFhS


#58
return all(1 if int(i)%2 == 0 else 0 for i in str(eval(dir()[0])[0]))

#65
#return all(True if int(i)%2 == 0 else False for i in str(eval(dir()[0])[0]))

#65
#n, = eval(dir()[0])
#n = str(n)
#return sum(1 for i in n if int(i)%2 == 0) == len(n)

#66
#evenDigitsOnly = lambda n: all(True if int(i)%2 == 0 else False for i in str(n))

#67
#evenDigitsOnly = lambda n: sum(1 for i in str(n) if int(i)%2 == 0) == len(str(n))

#69
#n, = eval(dir()[0])
#n = str(n)
#return all(True if int(i)%2 == 0 else False for i in n)

#69
#def evenDigitsOnly(n):
#    n = str(n)
#    return sum(1 for i in n if int(i)%2 == 0) == len(n)
