class Solution:
    def stringMirror(self, str : str) -> str:
        ans = []
        ans.append(str[0])
        
        for i in range(1, len(str)):
            if str[i - 1] > str[i] or (i > 1 and str[i] == str[i - 1]):
                ans.append(str[i])
            else:
                break
        
        curr = ''.join(ans)
        return curr + curr[::-1]
