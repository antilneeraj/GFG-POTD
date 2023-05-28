<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Nth node from end of linked list<br><br>

```python
def getNthFromLast(head,n):
    dataArr=[]
    while head:
        dataArr.append(head.data)
        head = head.next

    length = len(dataArr)
    return dataArr[length-n] if length >= n else -1
```
