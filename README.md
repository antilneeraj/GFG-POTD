<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Max Coins<br><br>

```python
from typing import List, Tuple

class Solution:
    def maxCoins(self, n, ranges):
        ranges.sort(key=lambda r: (r[1], r[0]))
        range_list = []
        max_coins = 0
        for range in ranges:
            max_coins = max(max_coins, self.get_maximum_coins_in_range(range_list, range[0]) + range[2])
            if not range_list or range_list[-1][1] < range[2]:
                range_list.append((range[1], range[2]))
        return max_coins

    def get_maximum_coins_in_range(self, range_list: List[Tuple[int, int]], end: int) -> int:
        lo, hi, idx = 0, len(range_list) - 1, -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if range_list[mid][0] <= end:
                idx = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return 0 if idx == -1 else range_list[idx][1]
```
