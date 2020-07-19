# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

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


def fun_nth_happy_number(n):
	count = 0
	for i in range(50):
		if(ishappynumber(i)):
			count += 1
			if (count == n):
				break
		return i
