# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().
def getkthDigit(x, n):
	# num = abs(x)
	res1 = x%10**(n+1)
	res2 = x%10**(n)
	dig = (res2-res1)/(10**n)
	return dig
def handtodice(hand):
	# your code goes here
	num = abs(hand)
	k1 = getkthDigit(num,2)
	k2 = getkthDigit(num,1)
	k3 = getkthDigit(num,0)
	m = (k1,k2,k3)
	return m
	# pass
