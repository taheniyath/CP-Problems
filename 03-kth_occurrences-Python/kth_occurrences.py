# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	dct = {}
	for i in s:
		if i not in dct.keys():
			dct[i] = 1
		else:
			dct[i] = dct[i] + 1
	dct1 = {k:v for k,v in sorted(dct.items(),key = lambda item:item[1])}
	l = [{dct1[k]:k}for k in dct1]
	l.reverse()
	a=l[n-1].values()
	r=list(a)[0]  
	return r


