# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	if n<0:
		n = -n
	l = list(map(int, str(n)))
	dct = {}
	count = 1
	for i in range(len(l) - 1):
		if l[i] == l[i+1]:
			count = 0
			if l[i] in dct:
				dct[l[i]] = dct[l[i]] + 1
			else:
				dct[l[i]] = 1
	if count == 1:
		l.sort()
		return l[0]
	dct1 = {}
	k = sorted(dct.keys())
	for i in k:
		dct1[i] = dct[i]
		dct1 = sorted(dct1.items(), key = lambda item:item[1], reverse = True)
	return dct1[0][0]
	# pass