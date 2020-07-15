"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    n = position
    if(n<=1):
        return n
    else:
        return(get_fib(n-1) + get_fib(n-2))
    # return -1