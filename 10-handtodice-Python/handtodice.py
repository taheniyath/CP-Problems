# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().
def getkthDigit(hand, n):
	num = abs(hand)
	res1 = num%10**(n+1)
	res2 = num%10**(n)
	dig = (res2-res1)/10**(n)
	return dig
def handtodice(hand):
	# your code goes here
	k1 = getkthDigit(hand,0)
	k2 = getkthDigit(hand,1)
	k3 = getkthDigit(hand,2)
	m = (k1,k2,k3)
	return m
	# pass
