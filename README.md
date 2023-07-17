<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - First non-repeating character in a stream<br><br>

```python
from collections import OrderedDict

class Solution:
	def FirstNonRepeating(self, A):
        counter = OrderedDict()  
        result = ""
    
        for char in A:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    
            unique_char = next((key for key, value in counter.items() if value == 1), "#")
            result += unique_char
    
        return result
```
