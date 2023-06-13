<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - K Largest Elements<br><br>

```python
class Solution:
	def kLargest(self,arr, n, k):
		arr = sorted(arr,reverse=True)
		return arr[:k]
```
