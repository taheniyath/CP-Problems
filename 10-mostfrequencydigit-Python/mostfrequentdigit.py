# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def occurrences(n,i):
	count = 0
	while (n):
		if(n%10 == 10):
			count += 1
		n = int(n/10)
	return count

def mostfrequentdigit(n):
	# your code goes here
	max = 1
	result =0
	s = str(n)
	for i in range(len(s)):
		count = occurrences(n, i)
		if(count >= max):
			max = count
			result = i
	return result
	# pass