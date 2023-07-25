def findSpiral(root):
    depthDict={0:[root.data]}
    elems=[root]
    newElems=[]
    depth=0
    while(len(elems)):
        depth+=1
        depthDict[depth]=[]
        for elem in elems:
            depthDict[depth].append(elem.left.data) if elem.left else None
            depthDict[depth].append(elem.right.data) if elem.right else None
            newElems.append(elem.left) if elem.left else None
            newElems.append(elem.right) if elem.right else None
        elems=newElems
        newElems=[]

    ans=[]
    for depth in depthDict:
        for elem in (depthDict[depth] if depth%2==1 else depthDict[depth][::-1]):
            ans.append(elem)
    return ans
