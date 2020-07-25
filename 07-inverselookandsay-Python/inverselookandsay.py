# Write the function inverseLookAndSay(a) that does the inverse of the previous problem, so that, in general:
#       inverseLookAndSay(lookAndSay(a)) == a
# Or, in particular:
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([]) == []
# inverseLookAndSay([(3,1)]) == [1,1,1]
# inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7]
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([(2,3),(1,8),(4,3)]) == [3,3,8,3,3,3,3])

def inverselookandsay(a):
	# Your code goes here
	l = len(a)
	l1 = []
	for i in range (l):
		if a[i] == ():
			return l1
		else:
			(m,n) = a[i]
			for i in range(m):
				l1.append(n)
	return l1
	# pass