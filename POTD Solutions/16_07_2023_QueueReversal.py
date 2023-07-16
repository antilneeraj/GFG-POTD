class Solution:
    def rev(self, q):
        stack = []
        while not q.empty():
            stack.append(q.get())
        while stack:
            q.put(stack.pop())
        return q
