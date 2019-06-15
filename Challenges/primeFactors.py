# Answer to primeFactors
# https://app.codesignal.com/challenge/Xa5wqxrtQB9e47Yeq

def prime(n):
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0: 
        return False
    
    i = 5
    while(i * i <= n) : 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i += 6
    return True 


def primeFactors(n):
    res = []
    if n != 1:
        i = 2
        while i < n//2:
            while prime(i) and n%i == 0:
                res.append(i)
                n /= i
            i += 1
        if n != 1:
            res.append(n)
    return res