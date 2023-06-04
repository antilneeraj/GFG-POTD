<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Reversing the equation<br><br>

```python
import re

class Solution:
    def reverseEqn(self, s):
        tokens = re.findall(r'\d+|\+|\-|\*|\/', s)
        reversed_tokens = tokens[::-1] 
        reversed_eqn = ''.join(reversed_tokens)  
        return reversed_eqn
```
