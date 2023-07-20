<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Non Repeating Character<br><br>

```python
class Solution:
    def nonrepeatingCharacter(self,s):
        mydict = dict()
        
        for letter in s:
            if(letter not in mydict): mydict[letter] = 0
            mydict[letter] += 1
        for letter in s:
            if(mydict[letter] == 1):
                return letter
        return '$'
```
