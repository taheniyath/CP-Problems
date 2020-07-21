# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	s = str(n)
	if(len(s)==1):
		return n
	elif(len(s) == 2):
		if s[0] <= s[1]:
			return int(s[0])
		else:
			return int(s[1])
	else:
		res = -1
		count = 0
		for i in range(len(s) -1):
			if(s[i] == s[i+1]):
				res = s[i]
				count += 1
		if count > 0:
			return int(res)
	# pass