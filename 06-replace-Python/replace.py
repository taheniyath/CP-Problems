# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	strng = ''
	i = 0
	l = len(s2)
	while i != len(s1):
		if s1[i:i+l2]==s2:
			strng += s3
			i = i+l2
		else:
			strng += s1[i]
			i = i+1
	return strng

