<<<<<<< HEAD
# Answer to isLucky
# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ


def isLucky(n):
    n = str(n)
    length = len(n)//2
    return sum(int(i) for i in n[:length]) == sum(int(i) for i in n[length:])
=======
# Answer to isLucky
# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ


def isLucky(n):
    n = str(n)
    length = len(n)//2
    return sum(int(i) for i in n[:length]) == sum(int(i) for i in n[length:])
>>>>>>> ea7bb9410c4da973ba9d0fff5b5025e66af029e4
