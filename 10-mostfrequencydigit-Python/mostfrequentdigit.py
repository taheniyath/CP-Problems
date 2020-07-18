# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def occurrences(x,i):
	count = 0
	while (x):
		if(x%10 == 10):
			count += 1
		x = int(x/10)
	return count

def mostfrequentdigit(n):
	# your code goes here
	max = 1
	s = str(n)
	for i in range(len(s)):
		count = occurrences(x, i)
		if(count >= max):
			max = count
			result = i
	return result
	# pass