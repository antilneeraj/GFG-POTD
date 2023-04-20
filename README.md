<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Bheem Wants Ladoos<br><br>

```python
class Solution:
    ans = 0

    def ladoos(self, root, home, k):
        self.ans = 0
        self.solve(root, home, k)
        return self.ans

    def solve(self, root, home, k):
        if root is None:
            return -1
        if root.data == home:  # add till k levels downstream
            self.add(root, k)
            return k-1  # will add k-1 downstream nodes from parent node of target
        
        rem = self.solve(root.right, home, k)  # found in right st - rem is catching k-1 
        if rem >= 0:
            self.ans += root.data  # adding the target's parent in sum;
            self.add(root.left, rem-1)  # since found on right,ie we need to target parent left st
            return rem-1 
        
        # try writing for left st as well.
        rem = self.solve(root.left, home, k)  # when we found the target in lst
        if rem >= 0:
            self.ans += root.data
            self.add(root.right, rem-1)
            return rem-1
        return -1


    def add(self, n, dist):
        if n is None or dist < 0:
            return
        self.ans += n.data
        # sum curr node and recur for left and right
        self.add(n.left, dist-1)
        self.add(n.right, dist-1)
```
