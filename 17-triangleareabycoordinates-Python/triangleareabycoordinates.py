# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
def triangleArea(s1,s2,s3):
	x = (s1+s2+s3)/2
	area = math.sqrt(x*(x-s1)*(X-s2)*(x-s3))
	return area
def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	x = math.sqrt((x2-x1)**(2) + (y2-y1)**(2))
	y = math.sqrt((x3-x2)**(2) + (y3-y2)**(2))
	z = math.sqrt((x1-x3)**(2) + (y1-y3)**(2))
	res = triangleArea(x,y,z)
	return res
	pass