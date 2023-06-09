<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Permutations of a given String<br><br>

```python
from itertools import permutations

class Solution:
    def find_permutation(self, S):
        ans = []
        perms = permutations(S)

        unique_perms = set(''.join(perm) for perm in perms)

        sorted_perms = sorted(unique_perms)

        for perm in sorted_perms:
            ans.append(''.join(perm))
            
        return ans
```
