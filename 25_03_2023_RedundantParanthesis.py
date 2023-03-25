class Solution:
    def removeBrackets(self, Exp):
        s = list(Exp)
        n = len(Exp)

        ans = [1] * (n+1)
        lasta = [-1] * (n+1)
        nxta = [-1] * (n+1)

        # last[i] = last op explored before index i ,
        l = -1
        for i in range(n):
            lasta[i] = l
            if s[i] in ['*', '+', '-', '/']:
                l = s[i]
        # nxta[i] = next operator explored after index i
        l = -1
        for i in range(n-1, -1, -1):
            nxta[i] = l
            if s[i] in ['*', '+', '-', '/']:
                l = s[i]

        st = []
        sign = [-1] * 256 # index of last occ of operators in exp
        mp = [0] * 256 # stores whether an op is present in sub_expresssion
        operand = ['*', '+', '-', '/']

        for p in range(n):
            for x in operand:
                if x == s[p]: # string the operators index if present
                    sign[ord(x)] = p
            if s[p] == '(':
                st.append(p)
            elif s[p] == ')':
                i = st.pop()
                j = p

                nxt = nxta[j]
                last = lasta[i]

                for x in operand:
                    if sign[ord(x)] >= i:
                        mp[ord(x)] = 1
                ok = 0

                # the sub exp we are comparing, checking if it has redundant braces
                if i > 0 and j+1 < n and s[i-1] == '(' and s[j+1] == ')':
                    ok = 1
                if mp[ord('+')] == 0 and mp[ord('*')] == 0 and mp[ord('-')] == 0 and mp[ord('/')] == 0: # no operators are present in b/w sub exp
                    ok = 1
                if last == -1 and nxt == -1: # if no opeators before i and after j
                    ok = 1
                if last == '/':
                    pass
                elif last == '-' and (mp[ord('+')] == 1 or mp[ord('-')] == 1):
                    pass
                elif mp[ord('-')] == 0 and mp[ord('+')] == 0:
                    ok = 1
                else:
                    if (last == -1 or last == '+' or last == '-') and (nxt == -1 or nxt == '+' or nxt == '-'):
                        ok = 1
                if ok == 1: # not req paranthese
                    ans[i] = 0 # not req ch
                    ans[j] = 0
        res = ""
        for i in range(n):
            if ans[i] > 0:
                res += s[i]
        return res