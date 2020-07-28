# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math
def digitCount(n):
    count = 0
    n = abs(n)
    while (n>=10):
        n = n//10
        count += 1
    return count + 1

def is_kaprekarNumber(n):
    p = digitCount(n)
    b = (n**2) % (10**p)
    c = (n**2 - b)/(10**p)
    if(b+c) == n:
        return True
    else:
        return False
def fun_nth_kaprekarnumber(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if(is_kaprekarNumber(guess)):
            found += 1
    return guess