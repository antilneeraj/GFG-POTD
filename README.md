<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Is Binary Number Multiple of 3<br><br>

```python
class Solution:
	def isDivisible(self, s):
		deci = int(s, 2)
		if deci % 3 == 0:
		    return 1
		return 0
```
