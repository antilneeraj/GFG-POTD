class Solution:
    def LPS(self, str):
        n = len(str)
        lps = [0] * n
        i = 1
        length = 0
        lps[0] = 0
        while i < n:
            if str[i] == str[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length == 0:
                    lps[i] = 0
                    i += 1
                else:
                    length = lps[length - 1]
        return lps
    
    def addMinChar (self, str1):
        orig = list(str1)
        temp = list(str1)
        temp.reverse()
        s = "".join(orig) + '#' + "".join(temp)
        n = len(s)
        lps = self.LPS(s)
        return len(str1) - lps[n-1]