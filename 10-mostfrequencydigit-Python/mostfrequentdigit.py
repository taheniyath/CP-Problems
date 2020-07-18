# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def occurrences(n,i):
	count = 0
	while (n):
		if(n%10 == i):
			count += 1
		n = int(n/10)
	return count

def mostfrequentdigit(n):
	# your code goes here
	s = str(n)
	if(len(s)==1):
		return n
	max = 1
	result =0
	
	for i in range(15):
		count = occurrences(n, i)
		if(count > max):
			max = count
			result = i
	return result
	# pass