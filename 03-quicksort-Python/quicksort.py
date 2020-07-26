"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	# Your code goes here
	a = []
	b = []
	d = []
	if len(array)>1:
		k = array[0]
		for i in array:
			if i<k:
				a.append(i)
			elif i==p:
				b.append(i)
			else:
				c.append(i)
		return sorted(a)+b+sorted(c)
	else:
		return array
	pass