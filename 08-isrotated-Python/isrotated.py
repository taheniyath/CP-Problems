# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	x = len(str1)
	y = len(str2)
	if (x != y):
		return 0
	temp = str1 + str2
	i = 0
	if temp[i:i+y] == str2:

		return True
	else:
		i = i+1
		return False

	# pass