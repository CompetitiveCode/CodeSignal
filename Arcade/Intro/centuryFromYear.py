#Answer to centuryFromYear - https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN

def centuryFromYear(year):
    result = year % 100
    if result != 0:
        result = 1
    result += year//100
    return result