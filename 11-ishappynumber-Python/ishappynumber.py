# ishappynumber(n) [10 pts]
# A happy number is a number defined by the following process: Starting with any positive integer, replace the 
# number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will 
# stay ), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 
# are happy numbers.

# Write the function ishappynumber(n) which takes a possibly-negative integer and returns True if it is happy and 
# False otherwise. Note that all numbers less than 1 are not happy. Here are some test assertions for you:
# assert(ishappynumber(-7) == False)
# assert(ishappynumber(1) == True)
# assert(ishappynumber(2) == False)
# assert(ishappynumber(97) == True)
# assert(ishappynumber(98) == False)
# assert(ishappynumber(404) == True)
# assert(ishappynumber(405) == False)

def squaresum(n):
	squaresum = 0
	while(n):
		squaresum += (n%10) * (n%10)
		n = int (n/10)
	return squaresum

def ishappynumber(n):
	# your code goes here 
	res1 = n
	res2 = n
	while (True):
		res1 = squaresum(res1)

		res2 = squaresum(squaresum(res2))
		if(res1!=res2):
			continue
		else:
			break
	return True

    # return False

	# pass