<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Frequency Game<br><br>

```python
def LargButMinFreq(arr,n):
    myDict=dict()
    for i in arr:
        if(i not in myDict): myDict[i] = 0
        myDict[i]+=1
    minFreq = min(myDict.values())
    return max(filter(lambda key: myDict[key] == minFreq, myDict.keys()))
    
```
