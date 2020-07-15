"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if(n<=1):
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    # return -1