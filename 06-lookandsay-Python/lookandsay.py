# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of 
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say 
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	# Your code goes here
	x = len(a)
	cout = 0
	l1 = []
	if (x == 0):
		return []
	else:
		for i in range (0, x-1):
			for j in range (i+1,x):
				if (a[i] == a[j]):
					cout = cout+1
				
			l1.extend((i,cout))
		return l1
	# pass