# Answer to matrixElementsSum
# https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr/


def matrixElementsSum(matrix):
    result = 0
    length = len(matrix[0])
    temp = [1 for i in range(length)]
    for i in matrix:
        for j in range(length):
            if temp[j] != 0:
                if i[j] == 0:
                    temp[j] = 0
                else:
                    result += i[j]
                    temp[j] = 1
    return result
