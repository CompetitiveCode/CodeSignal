# Answer to makeArrayConsecutive2
# https://app.codesignal.com/challenge/2w6tp2Lxk6T5QzZxq

s, = eval(dir()[0])
return max(s)-min(s)+1-len(s)

#66
#s, = eval(dir()[0])
#return sum(1 for i in range(min(s),max(s)+1) if i not in s)
