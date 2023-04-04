class Solution():
    def lexicographicallyLargest(self, a, n):
        i = 0
 
        while i < n:
            j = i + 1
            while j < n and a[j] % 2 == a[j - 1] % 2:
                j += 1
                
            a[i:j] = sorted(a[i:j], reverse=True)
            i = j
        
        return a
