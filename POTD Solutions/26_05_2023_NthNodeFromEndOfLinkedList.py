def getNthFromLast(head,n):
    dataArr=[]
    while head:
        dataArr.append(head.data)
        head = head.next

    length = len(dataArr)
    return dataArr[length-n] if length >= n else -1
