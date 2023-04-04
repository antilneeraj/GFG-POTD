class Solution:
    def __init__(self, s):
        self.shop = s
    
    def find(self, n, k):
        cnt = 0
        s = 0
        e = n
        ans = None
        
        while k:
            ans = -1
            s = 0
            while s < e:
                mid = (s + e) // 2
                choc = self.shop.get(mid)
                if choc == -1:
                    ans = -1
                if choc > k:
                    e = mid
                else:
                    ans = choc
                    s = mid + 1
            
            if ans == -1:
                break
            
            cnt += k // ans
            k = k % ans
        
        return cnt