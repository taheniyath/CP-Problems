# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



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
    else:return False

def fun_nearestkaprekarnumber(n):
    bigger = n
    smaller = n
    counter_up = 0
    counter_down = 0
    while not is_kaprekarNumber(bigger):
        bigger += 1
        counter_up += 1
    while not is_kaprekarNumber(smaller):
        smaller -= 1
        counter_down += 1
    if counter_up < counter_down:
        return bigger
    else:
        return smaller