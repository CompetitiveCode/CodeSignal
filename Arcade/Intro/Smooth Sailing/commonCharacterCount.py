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
