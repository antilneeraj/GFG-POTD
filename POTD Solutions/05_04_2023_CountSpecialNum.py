class Solution:
    def countSpecialNumbers(self, N, arr):
        freq = {}
        uniq = set()
        maximum = 0

        for i in range(N):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
            uniq.add(arr[i])
            maximum = max(maximum, arr[i])

        special = set()
        for z in uniq:
            for i in range(2 * z, maximum+1, z):
                if i in uniq:
                    special.add(i)

        ans = 0
        for x in freq.items():
            if x[1] > 1:
                ans += x[1]
            elif x[0] in special:
                ans += 1
        
        return ans