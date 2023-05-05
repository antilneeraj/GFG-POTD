<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Good Subtrees<br><br>

```python
class Solution:
    def help(self, root, k, ans):
        mm, mm2, mm3 = {}, {}, {}
        if root.left:
            mm2 = self.help(root.left, k, ans)
        if root.right:
            mm3 = self.help(root.right, k, ans)
        if len(mm2) > k:
            return mm2
        if len(mm3) > k:
            return mm3
        mm[root.data] = 1
        for x in mm2:
            mm[x] = mm.get(x, 0) + mm2[x]
        for x in mm3:
            mm[x] = mm.get(x, 0) + mm3[x]
        if len(mm) <= k:
            ans[0] += 1
        return mm
    
    def goodSubtrees(self, root, k):
        ans = [0]
        self.help(root, k, ans)
        return ans[0]
```
