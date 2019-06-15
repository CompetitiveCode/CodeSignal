<<<<<<< HEAD
# Answer to almostIncreasingSequence
# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG


def almostIncreasingSequence(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True

# I had to take help to solve this.
# And this is taken from a user pharfenmeister
=======
# Answer to almostIncreasingSequence
# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG


def almostIncreasingSequence(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True

# I had to take help to solve this.
# And this is taken from a user pharfenmeister
>>>>>>> ea7bb9410c4da973ba9d0fff5b5025e66af029e4
