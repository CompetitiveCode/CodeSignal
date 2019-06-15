#Answer to makeArrayConsecutive2 - https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

def makeArrayConsecutive2(statues):
    return max(statues)-min(statues)-len(statues)+1