# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	x1 = str(x)
	y1 = str(y)
	l1 = len(x1)
	l2 = len(y1)
	if(x1 == y1[ : :-1]):
		return True
	if (l1 != l2):
		return 0
	temp = x1 + y1
	if y1 in temp:
		return True
	else:
		return False
	# pass  