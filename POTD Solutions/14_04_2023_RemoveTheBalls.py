from typing import List

class Solution:
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        st = []
        for i in range(N):
            if len(st):
                index = st[-1]
                if color[index] == color[i] and radius[index] == radius[i]:
                    st.pop()
                else:
                    st.append(i)
            else:
                st.append(i)
        return len(st)
