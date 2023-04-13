class Solution:
    def minDifference(self, N, A): 
        arr = [0] * N
        arr[0] = A[0]
        for i in range(1, N):
            arr[i] = A[i] + arr[i - 1]
        ans = float('inf')
        for i in range(2, N - 1):
            index = self.binary_search(arr, 0, i - 1, arr[i - 1], 0)
            w = arr[index]
            x = arr[i - 1] - w
            index = self.binary_search(arr, i, N - 1, arr[N - 1], arr[i - 1])
            y = arr[index] - arr[i - 1]
            z = arr[N - 1] - arr[index]
            ans = min(ans, max(w, x, y, z) - min(w, x, y, z))
        return ans

    def binary_search(self, arr, low, high, _sum, temp):
        mid, index = -1, -1
        first, second, diff = float('inf'), float('inf'), float('inf')
        while low <= high:
            mid = (low + high) // 2
            first = arr[mid] - temp
            second = _sum - arr[mid]
            if abs(first - second) < diff:
                index = mid
                diff = abs(first - second)
            if first < second:
                low = mid + 1
            else:
                high = mid - 1
        return index
