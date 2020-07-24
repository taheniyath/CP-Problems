# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	if(n==0):
		return s

	elif(n>0):
		n = n % len(s)
		return s[n:] + s[:n]
	elif(n<0):
		n = abs(n)
		n = n % len(s)
		return s[len(s)-n:] + s[:len(s)-n]
	# elif(n>0):
	# 	firstl = s[0 : n]
	# 	secondl = s[n : ]
	# 	res = (secondl + firstl)
	# 	return res
	# elif(n<0):
	# 	x = len(s) 
	# 	firstr = s[0 : x-n]
	# 	secondr = s[x-n: ]
	# 	res = (secondr + firstr)
	# 	return res

	# return s

