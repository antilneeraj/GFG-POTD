class Solution:
    def arrange(self,arr, n): 
        for i in range(n):
            arr[i] += (arr[arr[i]] % n) * n
    
        for i in range(n):
            arr[i] = arr[i] // n
    
        return arr
