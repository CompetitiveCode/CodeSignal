# Answer to isLucky
# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ


def isLucky(n):
    n = str(n)
    length = len(n)//2
    return sum(int(i) for i in n[:length]) == sum(int(i) for i in n[length:])
