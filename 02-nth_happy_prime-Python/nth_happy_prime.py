# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def squaresum(n):
	squaresum = 0
	while(n):
		squaresum += (n%10) * (n%10)
		n = int (n/10)
	return squaresum


def ishappynumber(n):
	res1 = n
	res2 = n
	while (True):
		res1 = squaresum(res1)
		res2 = squaresum(squaresum(res2))
		if(res1 != res2):
			continue
		else:
			break
	return (res1 == 1)

def isprime(n):
	if(n<=1):
		return False

def fun_nth_happy_prime(n):
	my_List = []
	for i in range(100):
		if(isprime(i) and ishappynumber(i)):
			my_List.append(i)

	return my_List[n]