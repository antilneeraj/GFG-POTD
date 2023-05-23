class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def constructBinaryTree(self, pre, pre_mirror, size):
        pos = size - 1
        index = 0
    
        def construct():
            nonlocal index, pos

            if index >= size:
                return None
    
            current = Node(pre[index])
    
            if current.data != pre_mirror[pos]:
                index += 1
                current.left = construct()
    
                index += 1
                current.right = construct()
    
            pos -= 1
            return current
    
        head = Node(None)
        head.left = construct()
    
        return head.left
