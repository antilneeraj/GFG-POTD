<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Minimum BST Sum Subtree<br><br>

```python


class Solution:
    def get(self, root, c):
        if not root:
            return 0

        c[0] += 1
        l = self.get(root.left, c)
        r = self.get(root.right, c)

        return l + r + root.data

    def populate(self, root, v):
        if not root:
            return

        self.populate(root.left, v)
        v.append(root.data)
        self.populate(root.right, v)

    def recur(self, target, root, res):
        if not root:
            return

        c = [0]
        sum = self.get(root, c)

        if sum == target:
            v = []
            self.populate(root, v)

            be = True
            for i in range(1, len(v)):
                if v[i - 1] >= v[i]:
                    be = False
                    break

            if be:
                res[0] = min(res[0], c[0])

        self.recur(target, root.left, res)
        self.recur(target, root.right, res)

    def minSubtreeSumBST(self, target, root):
        sum = [1e9]
        self.recur(target, root, sum)
        return int(sum[0]) if sum[0] != 1e9 else -1
```
