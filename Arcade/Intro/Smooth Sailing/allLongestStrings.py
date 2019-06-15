# Answer to allLongestStrings
# https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL


def allLongestStrings(inputArray):
    temp = [len(i) for i in inputArray]
    m = max(temp)
    return [i for i in inputArray if len(i) == m]
