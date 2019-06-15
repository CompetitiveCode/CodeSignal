<<<<<<< HEAD
# Answer to commonCharacterCount
# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32


def commonCharacterCount(s1, s2):
    letters, res = {}, 0
    for i in s1:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return sum(min(s2.count(i),letters[i]) for i in letters)
=======
# Answer to commonCharacterCount
# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32


def commonCharacterCount(s1, s2):
    letters, res = {}, 0
    for i in s1:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return sum(min(s2.count(i),letters[i]) for i in letters)
>>>>>>> ea7bb9410c4da973ba9d0fff5b5025e66af029e4
