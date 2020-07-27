# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.
def iseven(n):
	r = []
	if n == 0:
		return 0
	else:
		temp = n%10
		if temp % 2 == 0:
			return iseven(n//10)*10 +temp
		else:
			return iseven(n//10)
			
def fun_recursion_onlyevendigits(l): 
	if not l:
		return []

	return [iseven(l[0])]+fun_recursion_onlyevendigits(l[1:])