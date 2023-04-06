class Solution:
    def equalSum(self,A, N):
        sum = 0
        for num in A:
            sum += num
        ans = -1
        left_sum = A[0]
        sum -= A[0]
        if sum == 0:
            return 1
        for i in range(1, N - 1):
            sum -= A[i]
            if left_sum == sum:
                ans = i + 1
                break
            left_sum += A[i]
        return ans