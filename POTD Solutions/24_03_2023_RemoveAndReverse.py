class Solution:
    def removeReverse(self, s):
        n = len(s)
        i = 0
        j = n - 1
        mp = {}
        for char in s:
            if char in mp:
                mp[char] += 1
            else:
                mp[char] = 1
        flag = True 
        while i <= j:
            if flag:
                if mp[s[i]] > 1:
                    mp[s[i]] -= 1
                    s = s[:i] + '0' + s[i+1:]
                    flag = False
                i += 1
            else:
                if mp[s[j]] > 1:
                    mp[s[j]] -= 1
                    s = s[:j] + '0' + s[j+1:]
                    flag = True
                j -= 1
        ans = ""
        for char in s:
            if char != '0':
                ans += char
        if flag:
            return ans
        else:
            return ans[::-1]