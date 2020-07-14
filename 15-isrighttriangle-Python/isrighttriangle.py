import math
# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	x = math.sqrt((x2-x1)**(2) +(y2-y1)**(2))
	y = math.sqrt((x3-x2)**(2) +(y3-y2)**(2))
	z = math.sqrt((x1-y3)**(2) +(y1-y3)**(2))
	x1 = x**(2)
	y1 = y**(2)
	z1 = z**(2)
	if(math.isclose(x1,(y1+z1)) or math.isclose(y1,(x1+z1)) or math.isclose(z1,(y1+x1)) ):
		return True
	else:
		return False

	# pass
