class Solution:
    def countSubstring(self, S): 
        cnt=0
        for i in range(len(S)):
            l=0
            u=0
            for j in range(i,len(S)):
                if(S[j]>='a' and S[j]<='z'):
                    l+=1
                else:
                    u+=1
                    
                if(l==u):
                    cnt+=1
                    
        return cnt
