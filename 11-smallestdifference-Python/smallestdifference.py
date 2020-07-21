# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	l = len(a)
	diff = 10**20
	if(l == 0):
		return -1
	for i in range(l-1):
		for j in range(i+1,l):
			if(a[i]-a[j]<diff):
				diff = a[i]-a[j]
	return diff
	pass 