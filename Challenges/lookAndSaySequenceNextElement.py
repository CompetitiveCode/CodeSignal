# Answer to lookAndSaySequenceNextElement
# https://app.codesignal.com/challenge/K3J68NkFj5Tbi8tJR


e, = eval(dir()[0])
e = str(e)
t = e[0]
i = 0
r = ''
for k in e:
    if k == t:
        i += 1
    else:
        r += str(i) + t
        t = k
        i = 1
return r+str(i)+t
