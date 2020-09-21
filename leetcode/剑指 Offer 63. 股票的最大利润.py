from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_value = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            ans = max(prices[i] - min_value, ans)
            if prices[i] < min_value:
                min_value = prices[i]

        return ans