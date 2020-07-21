# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2



def isprime(n):
	if(n>1):
		for i in range(2,n):
			if((n%i) == 0):
				return False
			else:
				return True


def ispalindrome(n):
	x = str(n)
	s = x[: : -1]
	if(s == x):
		return True
	else:
		return False
def fun_nth_palindromic_prime(n):
	my_List = []
	for i in range(10000000):
		if(isprime(i)):
			if(ispalindrome(i)):
				my_List.append(i)
	return my_List[n]