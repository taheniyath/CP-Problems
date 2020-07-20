# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	l1 = len(a)
	if(l1==0):
		return None
	if l1 % 2 == 0:
		med1 = a[l1//2]
		med2 = a[l1//2-1]
		median = (med1 +med2)/2
		return median
	else:
		median = a[l1//2]
		return median
	pass