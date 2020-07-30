# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math
def digitCount(n):
    if n == 0: 
        return 1
    count = 0
    n = abs(n)
    while (n>=0):
        n = n//10
        count += 1
    return count 

def sumPartition(n, partitionSize):
    lPart = 0
    rPart = 0
    m = n
    for i in range(partitionSize):
        nthDigit = m%10
        rPart += nthDigit * (10 ** i)
        m //= 10
    if rPart == 0:
        return -1
    lPart = (n - rPart) // (10 ** partitionSize)
    return lPart + rPart

def is_kaprekarNumber(n):
    square = n**2
    numDigits = digitCount(square)
    for i in range(numDigits):
        if sumPartition(square, i+1) == n:
            return True
    return False
def fun_nth_kaprekarnumber(n):
    found = 0
    guess = 0
    while found <= n: 
        guess += 1
        if(is_kaprekarNumber(guess)):
            found += 1
    return guess