<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - CamelCase Pattern Matching<br><br>

```python
class Solution:
    def CamelCase(self, N, Dictionary, Pattern):
        self.ans = []  # Change to instance variable
        root = self.Trie()
        self.build(Dictionary, root)
        self.find(Pattern, root)
        
        self.ans.sort()
        if not self.ans:
            self.ans.append("-1")
        return self.ans
    
    def build(self, a, root):
        for word in a:
            temp = root
            for i in range(len(word)):
                if word[i].isupper():
                    if temp.ch[ord(word[i]) - ord('A')] is None:
                        temp.ch[ord(word[i]) - ord('A')] = self.Trie()
                    temp = temp.ch[ord(word[i]) - ord('A')]
            temp.al.append(word)
    
    def find(self, s, root):
        for i in range(len(s)):
            if root.ch[ord(s[i]) - ord('A')] is None:
                return 0
            root = root.ch[ord(s[i]) - ord('A')]
        self.printAllWords(root)
        return 1
    
    def printAllWords(self, root):
        for word in root.al:
            self.ans.append(word)  # Use self.ans instead of ans
        for i in range(26):
            child = root.ch[i]
            if child is not None:
                self.printAllWords(child)
    
    class Trie:
        def __init__(self):
            self.ch = [None] * 26
            self.al = []
```
