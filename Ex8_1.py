t = [1,2,3,4,5,6]
def chop(t):
	del t[0]
	del t[len(t)-1]
	
def middle(t):
	return t[1:(len(t)-1)]
	
s = middle(t)
