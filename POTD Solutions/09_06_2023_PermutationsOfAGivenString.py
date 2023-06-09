from itertools import permutations

class Solution:
    def find_permutation(self, S):
        ans = []
        perms = permutations(S)

        unique_perms = set(''.join(perm) for perm in perms)

        sorted_perms = sorted(unique_perms)

        for perm in sorted_perms:
            ans.append(''.join(perm))
            
        return ans
