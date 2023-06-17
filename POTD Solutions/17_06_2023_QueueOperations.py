class Solution:
    def insert(self, q, k): 
        q.append(k)

    def findFrequency(self, q, k):
        return q.count(k)
