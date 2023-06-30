class Solution:
	def isDivisible(self, s):
		deci = int(s, 2)
		if deci % 3 == 0:
		    return 1
		return 0
