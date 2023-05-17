class Solution:
    def isPossible(self, n, m, s):
        t_l = 0
        t_r = 0
        t_u = 0
        t_d = 0
        f_lr = 0
        f_ud = 0
        
        for i in range(len(s)):
            if s[i] == 'L':
                f_lr += 1
            elif s[i] == 'R':
                f_lr -= 1
            elif s[i] == 'U':
                f_ud += 1
            else:
                f_ud -= 1
            
            if f_lr >= 0:
                t_l = max(t_l, f_lr)
            else:
                t_r = min(t_r, f_lr)
            
            if f_ud >= 0:
                t_u = max(t_u, f_ud)
            else:
                t_d = min(t_d, f_ud)
        
        if t_l - t_r < m and t_u - t_d < n:
            return 1
        
        return 0
